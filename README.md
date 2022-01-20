# bangla-language

atom config.cson should look like this (atom-shell-commands package)

"*":
  "atom-shell-commands":
    commands: [
      {
        name: "en-to-bn"
        command: "en-to-bn.bat"
        arguments: []
        options:
          cwd: "{FileDir}/.."
          keymap: "ctrl-2"
      }
    ]
  core:
    telemetryConsent: "limited"
    themes: [
      "atom-dark-ui"
      "atom-dark-syntax"
    ]
    uriHandlerRegistration: "always"
  editor:
    preferredLineLength: 120
    softWrap: true
  "exception-reporting":
    userId: "3b5b08c5-cef2-4089-a648-809297c68b6d"
  welcome:
    showOnStartup: false
  wordcount:
    alwaysOn: true
    noextension: true
