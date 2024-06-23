# HideYourTracks

HideYourTrack is a project inspired by typoer, a previous project I found on GitHub.

What does it do?
- HYT takes input that you put inside a set text file, and will type it as though it's a human. Making errors along the way(correcting them too). The typing speed at which HYT types at can be customized to any WPM you desire :)
- Unlike typoer, it has better error correction and also supports latin characters that would not process correctly in typoer! 

Not sure if non latin characters work, you can try getting it functional. Make sure to make a pr if you manage to get something like Chinese Traditional working!!!

## Prerequisites

Python(obviously)

Path variable for python being set beforehand is **strongly** suggested!

Use [pip](https://pip.pypa.io/en/stable/) to install the requirements from requirements.txt

```bash
pip install -r requirements.txt
```

## Variables(line 55)
```wpm=55``` typing speed

```accuracy=0.9``` accuracy of the intentional mistakes HYT will make for you

```wait_key=''``` do not change this
## Usage
- cd to the directory the files have been installed
- Place the text you want HideYourTracks to type inside loremipsum.txt
- Edit the file paths inside HideYourTracks.py on lines 54 
- Ensure variables on line 55 are good

Run the following command while in the right directory
```bash
python hideyourtracks.py 
```

To stop HYT, please simply click on cli you used to exec and do "control + C"


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)

## Ethical implications
- This is just a POC, don't go too crazy :)

## Credits
- Thank you to georgetian3 for the original project insipiration
- JasonFR71 for creation
