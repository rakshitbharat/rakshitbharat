import os
import glob

def read_md_files():
    # Get all .md files in the current directory
    md_files = glob.glob('./*.md')
    
    # Open output file
    with open('output.txt', 'w', encoding='utf-8') as outfile:
        # Iterate through each .md file
        for md_file in md_files:
            # Write the filename as a header
            outfile.write(f"# Content of {md_file}\n\n")
            
            # Read and write the content of the .md file
            with open(md_file, 'r', encoding='utf-8') as infile:
                outfile.write(infile.read())
            
            # Add a separator between files
            outfile.write('\n\n' + '-'*80 + '\n\n')

    print(f"Content of {len(md_files)} Markdown files has been written to output.txt")

if __name__ == "__main__":
    read_md_files()