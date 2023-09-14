# -*- coding: utf-8 -*-
from utils.common_utils import *


def get_demo_air_quality(node_id, node_num):
    air_quality_data = []

    # Define the normal ranges for each parameter
    normal_ranges = {
        "area": ["Dubai", "Riyadh", "Hangzhou"],
        "nodeId": ["node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10"],
        "temperature": (20.0, 30.0),  # Example: 20°C to 30°C
        "humidity": (30.0, 60.0),  # Example: 30% to 60%
        "volume": (100.0, 500.0),  # Example: 100 units to 500 units
        "pm10": (0.0, 100.0),  # Example: 0 µg/m³ to 100 µg/m³
        "pm25": (0.0, 50.0),  # Example: 0 µg/m³ to 50 µg/m³
        "so2": (0.0, 10.0),  # Example: 0 ppm to 10 ppm
        "no2": (0.0, 20.0),  # Example: 0 ppm to 20 ppm
        "co": (0.0, 5.0),  # Example: 0 ppm to 5 ppm
        "status": {
            "running": 70,
            "unknown stop": 10,
            "not available": 9,
            "pause": 8,
            "momentary stop": 7,
            "other technical malfunction": 6,
            "post-processing": 3,
            "preparation": 2,
            "maintenance": 1,
        },
    }

    if node_id is None and node_num is None:
        node_num = 5
    elif node_id is not None:
        node_num = 1

    available_node_ids = normal_ranges["nodeId"]  # Initialize available_node_ids

    # Generate random data for node_num sets of air quality parameters
    for _ in range(node_num):
        air_quality_entry = {}
        for param, value_range in normal_ranges.items():
            if param == "nodeId":
                if available_node_ids:
                    air_quality_entry["nodeId"] = node_id if node_id else random.choice(available_node_ids)
                    available_node_ids.remove(air_quality_entry["nodeId"])  # Remove chosen nodeId
            elif param == "status":
                # Select a random status based on the provided weights
                statuses = list(value_range.keys())
                weights = list(value_range.values())
                air_quality_entry[param] = random.choices(statuses, weights=weights, k=1)[0]
            elif isinstance(value_range, tuple):
                min_value, max_value = value_range
                air_quality_entry[param] = random_float(min_value, max_value)
            elif isinstance(value_range, list):
                air_quality_entry[param] = random.choice(value_range)
        air_quality_data.append(air_quality_entry)

    return air_quality_data


def get_demo_water_meter(node_id, node_num):
    water_meter_data = []

    # Define the normal ranges for each parameter
    normal_ranges = {
        "area": ["Dubai", "Riyadh", "Hangzhou"],
        "nodeId": ["node1", "node2", "node3", "node4", "node5", "node6", "node7", "node8", "node9", "node10"],
        "water_usage": (20.0, 2000.0),  # Example: 20°C to 30°C
        "vibration_data": (2.0, 25.0),  # Example: 30% to 60%
        "status": {
            "running": 70,
            "unknown stop": 10,
            "not available": 9,
            "pause": 8,
            "momentary stop": 7,
            "other technical malfunction": 6,
            "post-processing": 3,
            "preparation": 2,
            "maintenance": 1,
        },
    }

    if node_id is None and node_num is None:
        node_num = 5
    elif node_id is not None:
        node_num = 1

    available_node_ids = normal_ranges["nodeId"]  # Initialize available_node_ids

    # Generate random data for node_num sets of air quality parameters
    for _ in range(node_num):
        water_meter_entry = {}
        for param, value_range in normal_ranges.items():
            if param == "nodeId":
                if available_node_ids:
                    water_meter_entry["nodeId"] = node_id if node_id else random.choice(available_node_ids)
                    available_node_ids.remove(water_meter_entry["nodeId"])  # Remove chosen nodeId
            elif param == "status":
                # Select a random status based on the provided weights
                statuses = list(value_range.keys())
                weights = list(value_range.values())
                water_meter_entry[param] = random.choices(statuses, weights=weights, k=1)[0]
            elif isinstance(value_range, tuple):
                min_value, max_value = value_range
                water_meter_entry[param] = random_float(min_value, max_value)
            elif isinstance(value_range, list):
                water_meter_entry[param] = random.choice(value_range)
        water_meter_data.append(water_meter_entry)

    return water_meter_data
