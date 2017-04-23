# Sort GNOME Shell Apps!
This simple shell script makes the GNOME Shell Apps Dashboard sort the apps into their respective categories based on the [FreeDesktop standard](https://standards.freedesktop.org/menu-spec/latest/apa.html).

## Results
A nicely sorted Apps Dashboard!

![Screenshot](http://i.imgur.com/2o2yIib.png)
_App icons are property of their respective owners._

## How to use?

*You may want to back up your dConf before doing this, just in case something goes wrong.*

1. Clone or download this repository from GitHub.
2. Flag `appfixer.sh` as executable.
3. Run `appfixer.sh` from a terminal.
4. Restart GNOME Shell by pressing `ALT+F2` and running the command `r`. Alternatively, you could restart your machine or log out/in to achieve this.
5. Enjoy!

## FAQ

#### Which versions of GNOME Shell does this work on?
I have used this on GNOME Shell v3.22 and GNOME Shell v3.24 successfully. There's a good chance the script will still work, but as always, be sure to back up your dConf before using scripts like this that modify the system configuration.

#### A category is missing!
I only implemented the most commonly used categories. To add new categories, see below about fixing unsorted apps.

#### How do I remove a category?
To remove a category, see below about fixing unsorted apps. GNOME Software allows you to both create and delete categories.

#### How to fix unsorted apps?
After applying the fix, some apps may not be sorted into categories. There's a good chance the app developer didn't include the categories in their `.desktop` file. This can be corrected by manually adding the app to the appropriate folder using GNOME Software. For more information, see [this post on the GNOME Blog](https://blogs.gnome.org/mclasen/2014/03/17/app-folder-configuration/).
