import sublime, sublime_plugin
import re

def replacements():
  return [
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
  ]

class SmartyPantsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for sel in self.view.sel():
      region = self.view.word(sel)
      text = self.view.substr(region)

      if text == "":
        continue

      # Transform these items manually because we need a regex.
      text = re.sub(r"\"(.*?)\"", r"“\1”", text)
      text = re.sub(r"'(.*?)'", r"‘\1’", text)
      text = re.sub(r"([\w\d]+)'", r"\1’", text)
      text = re.sub(r"([\d.,]+) x ([\d.,]+)", r"\1 × \2", text)

      for pair in replacements():
        text = text.replace(pair[0], pair[1])

      self.view.replace(edit, region, text)

class UnsmartyPantsCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for sel in self.view.sel():
      region = self.view.word(sel)
      text = self.view.substr(region)

      if text == "":
        continue

      text = text.replace("×", "x")

      for pair in replacements():
        text = text.replace(pair[1], pair[0])

      self.view.replace(edit, region, text)
