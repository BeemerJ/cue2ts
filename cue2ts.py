def parse_cue_sheet(cue_file):
    timestamps = []
    songs = []
    performers = []
    with open(cue_file, 'r') as f:
        lines = f.readlines()

    track_info = {'PERFORMER': '', 'TITLE': ''}  # Initialize track info
    for line in lines:
        if line.startswith('    INDEX 01'):
            parts = line.split()
            try:
                timestamp = parts[-1][:5]  # Extract only HH:MM:SS
                timestamps.append(timestamp)
                songs.append(track_info['TITLE'])
                performers.append(track_info['PERFORMER'])
            except ValueError:
                print("Error parsing line:", line)
        elif line.strip().startswith('PERFORMER'):
            # Extract performer name
            track_info['PERFORMER'] = line.split('PERFORMER')[1].strip().strip('"')
        elif line.strip().startswith('TITLE'):
            # Extract song title
            title = line.split('TITLE')[1].strip().strip('"')
            if title.endswith('\\'):
                # If the title spans multiple lines
                track_info['TITLE'] += title[:-1]  # Remove trailing \
            else:
                # If the title is on a single line
                track_info['TITLE'] = title

    return timestamps, songs, performers


def convert_to_youtube_timestamp(timestamps, songs, performers, output_file):
    with open(output_file, 'w') as f:
        for i in range(len(timestamps)):
            f.write(f"{timestamps[i]} {performers[i]} - {songs[i]}\n")

if __name__ == "__main__":
    cue_file = input("Enter the path to the cue file... ")
    output_file = input("Enter the path for the output timestamp file... ")

    timestamps, songs, performers = parse_cue_sheet(cue_file)
    convert_to_youtube_timestamp(timestamps, songs, performers, output_file)

    print("Conversion complete!")
    
else:
    print("Error during conversion.")