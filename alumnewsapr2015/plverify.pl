use Mail::VRFY;
 my $email = shift;
 unless(defined($email)){
   print "email address to be tested: ";
   chop($email=<STDIN>);
 }
 my $code = Mail::VRFY::CheckAddress($email);
 my $english = Mail::VRFY::English($code);
 if($code){
   print "Invalid email address: $english  (code: $code)\n";
 }else{
   print "$english\n";
 }
