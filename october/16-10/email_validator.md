Email Validator
Given a string, determine if it is a valid email address using the following constraints:

It must contain exactly one @ symbol.
The local part (before the @):
Can only contain letters (a-z, A-Z), digits (0-9), dots (.), underscores (_), or hyphens (-).
Cannot start or end with a dot.
The domain part (after the @):
Must contain at least one dot.
Must end with a dot followed by at least two letters.
Neither the local or domain part can have two dots in a row.
Pruebas:
validate("a@b.cd") should return True.
validate("hell.-w.rld@example.com") should return True.
validate(".b@sh.rc") should return False.
validate("example@test.c0") should return False.
validate("freecodecamp.org") should return False.
validate("develop.ment_user@c0D!NG.R.CKS") should return True.
validate("hello.@wo.rld") should return False.
validate("hello@world..com") should return False.
validate("develop..ment_user@c0D!NG.R.CKS") should return False.
validate("git@commit@push.io") should return False.