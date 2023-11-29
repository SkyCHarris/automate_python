
#! Project: Phone Number and Email Address Extractor

# Say you have the boring task of finding every phone number and email address in a long web page or document
# If you manually scroll through the page, you might end up searching for a long time
# But if you had a program that could search the text in your clipboard for phone numbers and email address, you could simply:
    # Press CTRL-A to select all the text
    # Press CTRL-C to copy it to the clipboard
    # Run your program
# It could then replace the text on the clipboard with just the phone numbers and email addresses it finds

# When tackling a new project it can be tempting to dive right into writing code
# But it's often best to step back and consider the bigger picture
# Let's draw up a high-level plan for what the program needs to do
    # No code yet- worry about that later
# ex.:

#* 1. Get the text off the clipboard
#* 2. Find all phone numbers and email addresses in the text
#* 3. Paste them onto the clipboard

# Now start thinking about how this might work in code

#* 1. Use pyperclip module to copy and paste strings
#* 2. Create 2 regexes, one for matching phone numbers and one for matching email addresses
#* 3. Find all matches, not just the first match, of both regexes
#* 4. Neatly format the matched strings into a single string to paste
#* 5. Display some kind of message if no matches were found in the text

# This list is like a roadmap for the project
# As we write the code, focus on each step separately
# Each step is fairly manageable and expressed in terms of things we know how to do already


