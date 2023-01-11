__author__ = "Artur Barseghyan <artur.barseghyan@gmail.com>"
__copyright__ = "2022-2023 Artur Barseghyan"
__license__ = "MIT"
__all__ = (
    "TEXT_DOCX",
    "TEXT_EML",
    "TEXT_PDF",
    "TEXT_TXT",
    "TEXT_EPUB",
    "TEXT_RTF",
    "TEXTS",
)


TEXT_DOCX = """
“How doth the little crocodile
    Improve his shining tail,
And pour the waters of the Nile
    On every golden scale!

“How cheerfully he seems to grin,
    How neatly spread his claws,
And welcome little fishes in
    With gently smiling jaws!”
"""

TEXT_EML = """
“Will you walk a little faster?” said a whiting to a snail.
“There’s a porpoise close behind us, and he’s treading on my tail.
See how eagerly the lobsters and the turtles all advance!
They are waiting on the shingle—will you come and join the dance?
Will you, won’t you, will you, won’t you, will you join the dance?
Will you, won’t you, will you, won’t you, won’t you join the dance?

“You can really have no notion how delightful it will be
When they take us up and throw us, with the lobsters, out to sea!”
But the snail replied “Too far, too far!” and gave a look askance—
Said he thanked the whiting kindly, but he would not join the dance.
Would not, could not, would not, could not, would not join the dance.
Would not, could not, would not, could not, could not join the dance.

“What matters it how far we go?” his scaly friend replied.
“There is another shore, you know, upon the other side.
The further off from England the nearer is to France—
Then turn not pale, beloved snail, but come and join the dance.
Will you, won’t you, will you, won’t you, will you join the dance?
Will you, won’t you, will you, won’t you, won’t you join the dance?”
"""

TEXT_PDF = """
         “Fury said to a
         mouse, That he
        met in the
       house,
     ‘Let us
      both go to
       law: I will
        prosecute
         you.—Come,
           I’ll take no
           denial; We
          must have a
        trial: For
      really this
     morning I’ve
    nothing
    to do.’
      Said the
      mouse to the
       cur, ‘Such
        a trial,
         dear sir,
            With
          no jury
        or judge,
       would be
      wasting
      our
      breath.’
        ‘I’ll be
        judge, I’ll
         be jury,’
             Said
         cunning
          old Fury:
          ‘I’ll
          try the
            whole
            cause,
              and
           condemn
           you
          to
           death.’”
"""

TEXT_TXT = """
“You are old, Father William,” the young man said,
    “And your hair has become very white;
And yet you incessantly stand on your head—
    Do you think, at your age, it is right?”

“In my youth,” Father William replied to his son,
    “I feared it might injure the brain;
But, now that I’m perfectly sure I have none,
    Why, I do it again and again.”

“You are old,” said the youth, “as I mentioned before,
    And have grown most uncommonly fat;
Yet you turned a back-somersault in at the door—
    Pray, what is the reason of that?”

“In my youth,” said the sage, as he shook his grey locks,
    “I kept all my limbs very supple
By the use of this ointment—one shilling the box—
    Allow me to sell you a couple?”

“You are old,” said the youth, “and your jaws are too weak
    For anything tougher than suet;
Yet you finished the goose, with the bones and the beak—
    Pray, how did you manage to do it?”

“In my youth,” said his father, “I took to the law,
    And argued each case with my wife;
And the muscular strength, which it gave to my jaw,
    Has lasted the rest of my life.”

“You are old,” said the youth, “one would hardly suppose
    That your eye was as steady as ever;
Yet you balanced an eel on the end of your nose—
    What made you so awfully clever?”

“I have answered three questions, and that is enough,”
    Said his father; “don’t give yourself airs!
Do you think I can listen all day to such stuff?
    Be off, or I’ll kick you down stairs!”
"""

TEXT_EPUB = """
“Speak roughly to your little boy,
    And beat him when he sneezes:
He only does it to annoy,
    Because he knows it teases.”
“I speak severely to my boy,
    I beat him when he sneezes;
For he can thoroughly enjoy
    The pepper when he pleases!”
"""

TEXT_RTF = """
“’Tis the voice of the Lobster; I heard him declare,
“You have baked me too brown, I must sugar my hair.”
As a duck with its eyelids, so he with his nose
Trims his belt and his buttons, and turns out his toes.”

[later editions continued as follows
When the sands are all dry, he is gay as a lark,
And will talk in contemptuous tones of the Shark,
But, when the tide rises and sharks are around,
His voice has a timid and tremulous sound.]

“I passed by his garden, and marked, with one eye,
How the Owl and the Panther were sharing a pie—”

[later editions continued as follows
The Panther took pie-crust, and gravy, and meat,
While the Owl had the dish as its share of the treat.
When the pie was all finished, the Owl, as a boon,
Was kindly permitted to pocket the spoon:
While the Panther received knife and fork with a growl,
And concluded the banquet—]
"""

TEXTS = {
    "docx": TEXT_DOCX,
    "eml": TEXT_EML,
    "epub": TEXT_EPUB,
    "pdf": TEXT_PDF,
    "rtf": TEXT_RTF,
    "txt": TEXT_TXT,
}
