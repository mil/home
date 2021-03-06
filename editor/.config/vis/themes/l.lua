local lexers = vis.lexers

local colors = {
	['background']       = '#e8e8e8',

  ['base00'] = '#ffffff',
  ['base01'] = '#e0e0e0',
  ['base02'] = '#c5c8c6',
  ['base03'] = '#888888',
  ['base04'] = '#969896',
  ['base05'] = '#373b41',
  ['base06'] = '#282a2e',
  ['base07'] = '#1d1f21',
  ['base08'] = 'red',
  ['base09'] = '#0c0c0c',
  ['base0A'] = '#0f5e2c',
  ['base0B'] = '#000000',
  ['base0C'] = '#3971ED',
  ['base0D'] = '#3971ED',
  ['base0E'] = 'blue',
  ['base0F'] = '#3971ED',
}

lexers.colors = colors

local fg = ',fore:'..colors.base05..','
local bg = ',back:'..colors.base00..','

lexers.STYLE_DEFAULT = bg..fg
lexers.STYLE_NOTHING = bg
lexers.STYLE_CLASS = 'fore:'..colors.base0A..',bold'
lexers.STYLE_COMMENT = 'fore:'..colors.base03..',italics'
lexers.STYLE_CONSTANT = 'fore:'..colors.base07
lexers.STYLE_DEFINITION = 'fore:'..colors.base0E
lexers.STYLE_ERROR = 'fore:'..colors.base08..',italics'
lexers.STYLE_FUNCTION = 'fore:'..colors.base0D
lexers.STYLE_KEYWORD = 'fore:'..colors.base0E..',bold'
lexers.STYLE_LABEL = 'fore:'..colors.base0A..',bold'
lexers.STYLE_NUMBER = 'fore:'..colors.base0E
lexers.STYLE_OPERATOR = 'fore:'..colors.base07
lexers.STYLE_REGEX = 'fore:'..colors.base0C
lexers.STYLE_STRING = 'fore:'..colors.base0B
lexers.STYLE_PREPROCESSOR = 'fore:'..colors.base0A..',bold'
lexers.STYLE_TAG = 'fore:'..colors.base0A..',bold'
lexers.STYLE_TYPE = 'fore:'..colors.base0A..',bold'
lexers.STYLE_VARIABLE = 'fore:'..colors.base0D..',bold'
lexers.STYLE_WHITESPACE = 'fore:'..colors.base02
lexers.STYLE_EMBEDDED = 'fore:'..colors.base0F
lexers.STYLE_IDENTIFIER = 'fore:'..colors.base09

lexers.STYLE_LINENUMBER = 'fore:'..colors.base09..',back:'..colors.base01
lexers.STYLE_CURSOR = 'fore:'..colors.base00..',back:'..colors.base05
lexers.STYLE_CURSOR_PRIMARY = 'fore:'..colors.base00..',back:'..colors.base0E
lexers.STYLE_CURSOR_LINE = 'back:'..colors.base01
lexers.STYLE_COLOR_COLUMN = 'back:'..colors.base01
lexers.STYLE_SELECTION = 'back:'..colors.base02
lexers.STYLE_STATUS = 'fore:'..colors.base04..',back:'..colors.base01
lexers.STYLE_STATUS_FOCUSED = 'fore:'..colors.base09..',back:'..colors.base01
lexers.STYLE_SEPARATOR = lexers.STYLE_DEFAULT
lexers.STYLE_INFO = 'fore:default,back:default,bold'
lexers.STYLE_EOF = 'fore:'..colors.base05
