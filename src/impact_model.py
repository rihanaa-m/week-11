"""
Event Impact Modeling Module

This module provides functions for modeling how events affect financial inclusion indicators.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


class EventImpactModel:
    """
    Model the impact of events on financial inclusion indicators.
    """
    
    def __init__(self, impact_matrix_path):
        """
        Initialize the impact model with an association matrix.
        
        Args:
            impact_matrix_path: Path to the CSV file containing the impact matrix
        """
        self.impact_matrix = pd.read_csv(impact_matrix_path)
        self.events = self._load_events()
        
    def _load_events(self):
        """Load event data from the impact matrix."""
        events = {}
        for idx, row in self.impact_matrix.iterrows():
            event_id = row['parent_id']
            if event_id not in events:
                events[event_id] = {
                    'impacts': [],
                    'event_date': row.get('observation_date'),
                    'event_name': row.get('indicator_event', 'Unknown')
                }
            events[event_id]['impacts'].append({
                'indicator': row['related_indicator'],
                'direction': row['impact_direction'],
                'estimate': row['impact_estimate'],
                'lag_months': row['lag_months'],
                'magnitude': row['impact_magnitude']
            })
        return events
    
    def calculate_event_impact(self, event_id, target_date, indicator=None):
        """
        Calculate the impact of an event on a specific date.
        
        Args:
            event_id: The ID of the event
            target_date: The date to calculate impact for
            indicator: Optional specific indicator to calculate impact for
            
        Returns:
            Dictionary of impacts by indicator
        """
        if event_id not in self.events:
            return {}
        
        event = self.events[event_id]
        event_date = pd.to_datetime(event['event_date'])
        target_date = pd.to_datetime(target_date)
        
        # Calculate time elapsed
        time_elapsed = (target_date - event_date).days / 30.44  # Convert to months
        
        impacts = {}
        for impact in event['impacts']:
            # Check if lag period has passed
            if time_elapsed >= impact['lag_months']:
                # Apply impact based on direction
                if indicator is None or impact['indicator'] == indicator:
                    impacts[impact['indicator']] = {
                        'direction': impact['direction'],
                        'estimate': impact['estimate'],
                        'lag_months': impact['lag_months'],
                        'time_elapsed': time_elapsed
                    }
        
        return impacts
    
    def calculate_total_impact(self, target_date, indicator=None):
        """
        Calculate total impact from all events up to a target date.
        
        Args:
            target_date: The date to calculate total impact for
            indicator: Optional specific indicator to calculate impact for
            
        Returns:
            Dictionary of total impacts by indicator
        """
        total_impacts = {}
        
        for event_id in self.events:
            event_impacts = self.calculate_event_impact(event_id, target_date, indicator)
            
            for ind, impact in event_impacts.items():
                if ind not in total_impacts:
                    total_impacts[ind] = {
                        'total_estimate': 0,
                        'event_count': 0,
                        'events': []
                    }
                
                # Add impact based on direction
                if impact['direction'] == 'increase':
                    total_impacts[ind]['total_estimate'] += impact['estimate']
                elif impact['direction'] == 'decrease':
                    total_impacts[ind]['total_estimate'] -= impact['estimate']
                
                total_impacts[ind]['event_count'] += 1
                total_impacts[ind]['events'].append({
                    'event_id': event_id,
                    'estimate': impact['estimate'],
                    'direction': impact['direction']
                })
        
        return total_impacts
    
    def apply_impact_to_baseline(self, baseline_value, impacts, indicator):
        """
        Apply calculated impacts to a baseline value.
        
        Args:
            baseline_value: The baseline value before impacts
            impacts: Dictionary of impacts from calculate_total_impact
            indicator: The indicator being modified
            
        Returns:
            The adjusted value after applying impacts
        """
        if indicator in impacts:
            total_impact = impacts[indicator]['total_estimate']
            return baseline_value + total_impact
        return baseline_value
    
    def get_event_timeline(self):
        """
        Get a timeline of all events with their dates.
        
        Returns:
            DataFrame of events sorted by date
        """
        event_data = []
        for event_id, event in self.events.items():
            event_data.append({
                'event_id': event_id,
                'event_name': event['event_name'],
                'event_date': event['event_date'],
                'num_impacts': len(event['impacts'])
            })
        
        return pd.DataFrame(event_data).sort_values('event_date')


def create_impact_scenarios(impact_model, scenarios):
    """
    Create different impact scenarios for forecasting.
    
    Args:
        impact_model: EventImpactModel instance
        scenarios: Dictionary of scenario adjustments
                   (e.g., {'optimistic': 1.2, 'base': 1.0, 'pessimistic': 0.8})
    
    Returns:
        Dictionary of scenario-specific impact matrices
    """
    scenario_matrices = {}
    
    for scenario_name, multiplier in scenarios.items():
        # Copy the original matrix
        scenario_matrix = impact_model.impact_matrix.copy()
        
        # Apply multiplier to impact estimates
        scenario_matrix['impact_estimate'] = scenario_matrix['impact_estimate'] * multiplier
        
        scenario_matrices[scenario_name] = scenario_matrix
    
    return scenario_matrices


if __name__ == "__main__":
    # Example usage
    print("Event Impact Modeling Module")
    print("This module provides functions for modeling event impacts on financial inclusion indicators.")
