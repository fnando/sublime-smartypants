# SmartyPants for Sublime Text

Better typography utility plugin. Based on [John Gruber's project](https://daringfireball.net/projects/smartypants/).

This is the replacement list:

```
("\"", "“"),
("\"", "”"),
("'", "‘"),
("'", "’"),
("...", "…"),
("---", "—"),
("--", "–"),
("<<", "«"),
(">>", "»"),
("1/2", "½"),
("1/4", "¼"),
("3/4", "¾"),
("1/7", "⅐"),
("1/9", "⅑"),
("1/10", "⅒"),
("1/3", "⅓"),
("2/3", "⅔"),
("1/5", "⅕"),
("2/5", "⅖"),
("3/5", "⅗"),
("4/5", "⅘"),
("1/6", "⅙"),
("5/6", "⅚"),
("1/8", "⅛"),
("3/8", "⅜"),
("5/8", "⅝"),
("7/8", "⅞"),
("(c)", "©"),
("(r)", "®"),
("(p)", "℗"),
("(tm)", "™"),
("+-", "±"),
("!=", "≠"),
("?!", "‽"),
```

Additionally, the pattern `[\d.,]+ x [\d.,]+` will also be replaced with `×`.

## Installation

### Setup Package Control Repository

1. Follow the instructions from https://sublime.fnando.com.
2. Open the command pallete, run “Package Control: Install Package“, then search
   for “SmartyPants“.

### Git Clone

Clone this repository into the Sublime Text “Packages” directory, which is
located where ever the “Preferences” -> “Browse Packages” option in sublime
takes you.

## Usage

Select the text you want to apply the replacement and run either “SmartyPants: Apply” or “SmartyPants: Undo” from the quick command palette.

You can assign a shortcuts by adding something like the following to your
keybindings file:

```json
[
  { "keys": ["ctr+s"], "command": "smarty_pants" },
  { "keys": ["ctr+shift+s"], "command": "unsmarty_pants" }
]
```

On macOS, these shortcuts are automatically defined.

## License

Copyright (c) 2020 Nando Vieira

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
