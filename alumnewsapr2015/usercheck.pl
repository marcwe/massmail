    use Mail::CheckUser qw(check_email last_check);

    my $email = 'marcweemail@pcom.edu';

    if(check_email($email)) {
        print "E-mail address <$email> is OK\n";
    } else {
        print "E-mail address <$email> isn't valid: ",
              last_check()->{reason}, "\n";
    }
