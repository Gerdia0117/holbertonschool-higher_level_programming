#!/usr/bin/python3
"""
Module for generating personalized invitation files from templates.
"""


def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and list of attendees.
    
    Args:
        template (str): The invitation template with placeholders
        attendees (list): List of dictionaries containing attendee information
    
    Returns:
        None: Creates output files named output_X.txt
    """
    # Check if template is a string
    if not isinstance(template, str):
        print("Error: Template is not a string")
        return
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print("Error: Attendees is not a list")
        return
    
    # Check if all items in attendees are dictionaries
    if attendees and not all(isinstance(item, dict) for item in attendees):
        print("Error: Attendees is not a list of dictionaries")
        return
    
    # Check if template is empty
    if not template:
        print("Template is empty, no output files generated.")
        return
    
    # Check if attendees list is empty
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for this attendee
        output_content = template
        
        # Replace placeholders with actual values or "N/A"
        placeholders = ["name", "event_title", "event_date", "event_location"]
        
        for placeholder in placeholders:
            placeholder_key = "{" + placeholder + "}"
            value = attendee.get(placeholder)
            
            # If value is None or missing, use "N/A"
            if value is None or value == "":
                value = "N/A"
            
            output_content = output_content.replace(placeholder_key, str(value))
        
        # Write to output file
        output_filename = f"output_{index}.txt"
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(output_content)
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
