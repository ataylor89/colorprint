# readme

## Escape sequences

Escape sequence is a term that I have encountered a lot. But for a long time, I didn't know what it means.

I suppose I had a rough idea. But I didn't have a definition at hand.

These days, I make a point of writing down definitions. I try to come up with a definition that is clear and instructive.

Here is a definition for the term "escape sequence".

    Definition: An escape sequence is a sequence of characters, that starts with a backslash, and signifies a special character or a command.

The newline character (\n) is an escape sequence. The tab character (\t) is an escape sequence. These are some common escape sequences.

But it so happens that there are many escape sequences that are not as well known as \n and \t.

If you want to print colored text in a terminal, you can use ANSI color codes. ANSI color codes are escape sequences.

My understanding is this: ANSI color codes are interpreted by terminals as formatting instructions. I think that many terminals (like Terminal in MacOS and other popular terminals) are able to interpret ANSI color codes and use them for formatting.

When I say terminal, I'm referring to terminal emulators.

Terminal is the default terminal emulator for MacOS. GNOME Terminal is the default terminal emulator for many Linux distributions.

Terminal emulator is another term that requires definition. Let's do that in the next section.

## Terminal emulators

Before MacBooks, before desktop computers, there were video terminals.

Video terminals were popular in the 1960s, the 1970s, and the 1980s.

Video terminals came with a keyboard for input and a screen for output.

I was able to find a picture of one by searching VT100 on Google. VT100 was a popular video terminal in the 1970s and 1980s.

You can see that they don't have a mouse. They don't have a windowing system (in which applications are displayed in graphical windows).

Instead, they have a text-based interface. The user interacts with the computer shell by means of keyboard input. The output gets shown on the screen.

In this sense, they are a lot like terminal emulators. They are a lot like Terminal (MacOS) and Gnome Terminal (Linux).

Terminal emulators are software programs that emulate the original video terminals.

I like this definition.

    Definition: A terminal emulator is a software program that emulates the original video terminals.

## Why is an escape sequence called an escape sequence?

Why is an escape sequence called an escape sequence? This is a good question.

An escape sequence causes a compiler or an interpreter to escape to a new mode. The backslash is recognized by the compiler or interpreter as the beginning of an escape sequence. It then processes the escape sequence according to the rules set out by a standard (like ANSI or Unicode).

The escape sequence \n gets converted to a byte with value 0x0A, or 10 in decimal, when using the UTF-8 character encoding system.

The escape sequence \t gets converted to a byte with value 0x09, or 9 in decimal, when using the UTF-8 character encoding system.

So you can see that a compiler, or interpreter, enters a new mode when it encounters an escape sequence. It has to look up the rules for interpreting the escape sequence, and interpret it accordingly.

An escape sequence escapes from the normal flow of parsing, compilation, or interpretation.

## What are ANSI color codes?

ANSI color codes are escape sequences that allow a programmer to write colored text and styled text to a terminal emulator.

I discovered them recently, and got really excited. I decided to write a program called colorprint.py to demonstrate how they work.

## Usage

The program colorprint.py can be used in the following way.

    % cd ~/Github/colorprint
    % ls 
    ansi.py		colorprint.py	README.md	settings.py
    % python colorprint.py "Hello world (black on orange)"
    Hello world (black on orange)
    % python colorprint.py -fg cyan -bg none "Hello world (cyan)"
    Hello world (cyan)
    % python colorprint.py -fg cyan -bg black "Hello world (cyan on black")
    Hello world (cyan on black)
    % python colorprint.py -fg green -bg black "Hello world (green on black")
    Hello world (green on black)

The file defaults.py can be edited to change the default colors. (At the time of writing, the default colors are black on orange.)

I might update ansi.py to include more color codes, over time. If I find more, then I'll probably update it, to include them.

## What does #! mean?

When we type the command `python colorprint.py "Hello world"` in Terminal, we are using the Python interpreter to execute the program.

What if we want to use the shell (Bash or Zsh) to execute the program? Is there a way to do this?

It turns out, there is.

All we have to do is add a shell directive at the top of the file.

The shell directive specifies which interpreter to use to interpret the script.

The shell directive `#!/usr/bin/python3` instructs the shell to use the python3 interpeter to interpret the script.

We can be a little more fancy. We can use the shell directive `#!/usr/bin/env python3` to locate the first occurrence of the python3 interpreter in the directories listed in the user's PATH variable, and to use this program as the interpeter.

Why would I use `#!/usr/bin/env python3` instead of the more direct `#!/usr/bin/python3`?

I actually have a reason for doing so.

The utility `/usr/bin/env` comes pre-installed with MacOS, and it always has the same path, that is, `/usr/bin/env`.

The python3 interpreter might not come pre-installed with MacOS. Sometimes, it can be found in the folder `/usr/bin`. But it actually depends on how you install it. If you install it using a package manager, then it might end up in a different location.

Thinking about it mathematically, we can say there is a 100% chance, or a near 100% chance, that the `env` utility will be found in `/usr/bin`.

But the chance that `python3` will be found in `/usr/bin` is lower than 100%. It actually depends on how you install it.

The shell directive `#!/usr/bin/env python3` gives us a stronger guarantee that the correct Python interpreter will be located.

If it's not installed on the system, then it won't be found.

But if it is installed on the system, then we have a higher chance of finding it, if we use the `#!/usr/bin/env python3` shell directive.

## How do I run colorprint.py using the shell?

We can run the program colorprint.py, directly, using the shell, by setting it executable, and then using the `./` syntax for running a script.

    % cd ~/Github/colorprint
    % chmod +x colorprint.py
    % ./colorprint.py "Hello world"
    Hello world

To make things even easier, we can create a symbolic link in a folder like ~/bin, and add this folder to the PATH variable.

    % mkdir ~/bin
    % cd ~/bin
    % ln -s ~/Github/colorprint/colorprint.py colorprint.py

The command (above) created the symbolic link. Now we have to add the following line to `~/.zprofile` to include `~/bin` in the PATH variable.

    % vi ~/.zprofile
    export PATH="/Users/<myusername>/bin:$PATH"

The export statement (above) adds the `~/bin` folder to the PATH variable, by prepending it to the PATH variable.

After making these changes, we can execute `~/.zprofile` to put the changes into effect, or cause `~/.zprofile` to run by opening a new tab in Terminal.

Finally, we can run `colorprint.py` without the `./` syntax.

    % colorprint.py "Hello world"
    Hello world

This way, we can run colorprint.py from any directory when we are using Terminal.

Just like we can use `echo` and `cd` and `ls` from any directory, we can also use `colorprint.py` from any directory, because it's in our PATH variable.

## Vocab

I think it helps to write down some of the vocabulary that we used in this document.

| Word/Phrase | Definition |
| ----------- | ---------- |
| ANSI | The organization that created ASCII; also, an 8-bit character encoding standard that extends the 7-bit ASCII character set |
| ASCII | A 7-bit character encoding standard created in 1963 |
| Character decoding | A system for converting code points into characters, and numeric data into text |
| Character encoding | A system for converting characters into code points, and text into numeric data |
| Escape sequence | A sequence of characters, that starts with a backslash, that signifies a special character or a command |
| Hashbang (#!) | A sequence of characters (#!) that introduces a shell directive, and is placed at the top of a file |
| PATH variable | An environment variable that consists of a list of directories, and is used for locating programs |
| Shell | A command-line interpreter (like Bash or Zsh) that allows a user to interact with the operating system; video terminals actually interacted with a shell program that ran on the host computer, just like terminal emulators interact with a shell program |
| Terminal emulator | A software program that emulates the original video terminals |
| Unicode | A character encoding standard created in the early 1990s, that has over 1 million code points, and supports many world languages |
| Video terminal | A device consisting of a keyboard and a screen that allows input and output with a computer, popular in the 1960s, 1970s, and 1980s |

I enjoyed learning about video terminals while writing this document. It helps to explain what a terminal emulator is.

I also enjoyed learning about escape sequences, and the ANSI color codes in particular.
