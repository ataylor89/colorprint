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
