def generate_invitations(template, attendees):
    """
    Generate personalized invitation files from a template and list of attendees.
    
    Args:
        template (str): Template string with placeholders
        attendees (list): List of dictionaries containing attendee data
    """
    
    # Check input types
    if not isinstance(template, str):
        print("Error: Template must be a string.")
        return
    
    if not isinstance(attendees, list):
        print("Error: Attendees must be a list of dictionaries.")
        return
    
    # Check if attendees is a list of dictionaries
    for attendee in attendees:
        if not isinstance(attendee, dict):
            print("Error: Attendees must be a list of dictionaries.")
            return
    
    # Handle empty template
    if not template.strip():
        print("Template is empty, no output files generated.")
        return
    
    # Handle empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return
    
    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        # Create a copy of the template for processing
        processed_template = template
        
        # Define the placeholders we expect
        placeholders = ['name', 'event_title', 'event_date', 'event_location']
        
        # Replace each placeholder with the corresponding value or "N/A"
        for placeholder in placeholders:
            placeholder_key = '{' + placeholder + '}'
            value = attendee.get(placeholder)
            
            # Handle None or missing values
            if value is None or value == "":
                replacement_value = "N/A"
            else:
                replacement_value = str(value)
            
            processed_template = processed_template.replace(placeholder_key, replacement_value)
        
        # Generate output filename
        output_filename = f"output_{index}.txt"
        
        # Write the processed template to the output file
        try:
            with open(output_filename, 'w') as output_file:
                output_file.write(processed_template)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")
