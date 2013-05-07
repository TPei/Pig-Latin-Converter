Pig-Latin-Converter
===================

converts a text to pig latin
with unit test

RESULTS:
"happy" -> "appyhay";
"duck" -> "uckday";
"flow" -> "owflay";
"fly" -> "flyay";
"egg" -> eggway";
"inbox" -> "inboxway";
"what the heck is this stuff" -> "atwhay ethay eckhay isway isthay uffstay ";
"what the heck is this stuff?" -> "atwhay ethay eckhay isway isthay uffstay? ";
"what the heck? is this stuff?" -> "atwhay ethay eckhay? isway isthay uffstay? ";

ISSUES:
- special characters are handled as if they were letter
- except the last special character directly at the end of a work (no spaces etc)

"what the heck,,,, is this stuf???" -> "atwhay ethay eck,,,hay, isway isthay uf??stay?"


future plan: converts entire text to pig latin
