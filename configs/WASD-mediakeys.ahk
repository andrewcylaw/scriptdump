; See https://www.autohotkey.com/docs/KeyList.htm
;     https://www.autohotkey.com/docs/Hotkeys.htm
; Emulates WASD V2 media key shortcuts

AppsKey & Delete:: Send {Media_Prev}
AppsKey & End::    Send {Media_Next}
AppsKey & PgUp::   Send {Volume_Up}
AppsKey & PgDn::   Send {Volume_Down}
AppsKey & Insert:: Send {Media_Play_Pause}
