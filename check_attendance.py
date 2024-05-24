import pandas as pd

def update_attendance(name):
    # Path to the attendance sheet
    attendance_sheet_path = "C:\\Users\\manis\\OneDrive\\Desktop\\source code\\attendance.xlsx"
    
    # Read existing attendance sheet or create a new one if it doesn't exist
    try:
        attendance_sheet = pd.read_excel(attendance_sheet_path, engine='openpyxl')

    except FileNotFoundError:
        attendance_sheet = pd.DataFrame(columns=['Serial Number', 'Name', 'Attendance'])
    
    # Check if the person is already in the attendance sheet and if their attendance is marked as 'Present'
    if (attendance_sheet['Name'] == name).any() and not (attendance_sheet.loc[attendance_sheet['Name'] == name, 'Attendance'] == 'Present').any():
        # Update the attendance to 'Present' for the person
        attendance_sheet.loc[attendance_sheet['Name'] == name, 'Attendance'] = 'Present'
        print("Attendance marked as 'Present' for", name)
    elif (attendance_sheet['Name'] == name).any():
        print("Attendance already marked as 'Present' for", name)
    else:
        # Get the maximum serial number and increment it by 1 for the new entry
        max_serial_number = attendance_sheet['Serial Number'].max() if not attendance_sheet.empty else 0
        new_serial_number = max_serial_number + 1
        
        # Add new entry with serial number and 'Present' attendance for the person
        new_entry = pd.DataFrame({'Serial Number': [new_serial_number], 'Name': [name], 'Attendance': ['Present']})
        attendance_sheet = attendance_sheet.append(new_entry, ignore_index=True)
        print("Attendance marked as 'Present' for", name)
    
    # Save the updated attendance sheet
    with pd.ExcelWriter(attendance_sheet_path, mode='w', engine='openpyxl') as writer:
        attendance_sheet.to_excel(writer, index=False)

# Example usage:
# Specify the name of the person for whom you want to mark attendance
#name = "gopal"  # Change this to the desired name

# Update attendance
#update_attendance(name)
