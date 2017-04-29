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
3. Run `python3 interactive.py` to start the interactive program.
4. Follow the instructions on-screen and make selections using the keyboard.
5. Enjoy!

#### Using the old shell script

1. Clone or download this repository from GitHub.
2. Flag `appfixer.sh` as executable.
3. Run `appfixer.sh` from a terminal.
4. Restart GNOME Shell by pressing `ALT+F2` and running the command `r`. Alternatively, you could restart your machine or log out/in to achieve this.
5. Enjoy!

## FAQ -- Updated

If you used the version of the script (`appfixer.sh`), then you should read the [old FAQ](https://github.com/BenJetson/gnome-dash-fix/blob/333cee8de4ba3397d6c17b8601c685a0b5991804/README.md).

#### Which versions of GNOME Shell does this work on?
I have used this on GNOME Shell v3.22 and GNOME Shell v3.24 successfully. The script should work on other shell versions, but every system varies.

#### A category is missing from defaults!
I only implemented what I considered to be the most commonly used categories as "defaults" in the interactive script (if I missed one, let me know). Luckily, you can add more category folders by selecting option `2` from the main menu. For new folders, the `TITLE` should be a human readable short title, and it will appear on the dashboard. The `CATEGORIES` should be one of the FreeDesktop categories (see below).

For information about the categories, see [FreeDesktop.org's reference page](https://standards.freedesktop.org/menu-spec/latest/apa.html).

#### How do I remove a category?
If you don't like one of the default categories, you can remove it. Select option `2` from the main menu and follow the on-screen instructions to remove that category from the list. Keep in mind that this will overwrite any previous custom categories.

If you're already enabled the category folders, you can run the script again to configure different folders. If you prefer, you can remove the category using GNOME Software instead -- see below about fixing unsorted apps.

#### How to fix unsorted apps?
After applying the fix, some apps may not be sorted into categories. There's a good chance the app developer didn't include the categories in their `.desktop` file. This can be corrected by manually adding the app to the appropriate folder using GNOME Software. For more information, see [this post on the GNOME Blog](https://blogs.gnome.org/mclasen/2014/03/17/app-folder-configuration/).


#### How does this work?
This script uses Python to handle the logic and gets `gsettings` to change the configuration files for you on the backend. For information about configuring categories using `gsettings`, see [the GNOME Wiki](https://wiki.gnome.org/HowDoI/AppFolders).
