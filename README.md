# Sort GNOME Shell Apps!
This simple shell script makes the GNOME Shell Apps Dashboard sort the apps into their respective categories based on the [FreeDesktop standard](https://standards.freedesktop.org/menu-spec/latest/apa.html).

## Results
A nicely sorted Apps Dashboard!

![Screenshot](http://i.imgur.com/2o2yIib.png)
_App icons are property of their respective owners._

## How to use?

*You may want to back up your dConf before doing this, just in case something goes wrong.*

#### Using the new beta interactive script

1. Clone or download the repository from GitHub.
2. Open a terminal and `cd` to the directory containing the files.
3. Flag `interactive.py` as executable: `chmod +x interactive.py`
4. Run the script: `./interactive.py`
4. Follow the instructions on-screen and make selections using the keyboard.
5. Enjoy!


#### Using the legacy shell script

1. Clone or download this repository from GitHub.
2. Open a terminal and `cd` to the directory containing the files.
3. Flag `appfixer.sh` as executable: `chmod +x ./appfixer.sh`
4. Run `./appfixer.sh` from a terminal.
5. Restart GNOME Shell by pressing `ALT+F2` and running the command `r`. Alternatively, you could restart your machine or log out/in to achieve this.
6. Enjoy!

## Got a problem?

Read the [Wiki FAQ](https://github.com/BenJetson/gnome-dash-fix/wiki/FAQ:-Interactive) to see if your problem has already been solved. If not, then [open an issue](https://github.com/BenJetson/gnome-dash-fix/issues/new).
