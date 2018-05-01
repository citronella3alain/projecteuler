#!/usr/bin/perl
# fib.pl
use strict; use warnings;
my @fibbase;

##Index of the first fibonacci term to contain more than 1000 digits
my $fibber;
my $len = length($fibber);
my $n = 1;
until ($len >= 1000){
	$fibber = join('', @{fib($n)});
	$len = length($fibber);
	print ("$n : \t $fibber\n");
	$n++;
}
print("$fibber\n");
sub fib{
	my $n = shift;
	if (exists($fibbase[$n])) {
		my @to_store_fib = @{$fibbase[$n]};
		return \@to_store_fib;
	}
	if ($n == 1){
		return [1];
	}
	elsif ($n == 2){
		return [1];
	}
	else {
		my $fib = add(fib($n-1), fib($n-2));
		my @to_store_fib = @{$fib};
		$fibbase[$n] = \@to_store_fib;
		return $fib;
	}
}
sub are_equal01{
	my ($ref_to_n, $m) = @_; # $m is 0 or 1
	my $size = @{$ref_to_n};
	return 0 if (@{$ref_to_n} != 1);
	return 1 if (${$ref_to_n}[@{$ref_to_n}-1] == $m);
	return 0;
}

sub add{
	my ($ref_to_n1, $ref_to_n2) = @_;
	my @n;
	my $carry = 0;
	while (@{$ref_to_n1} && @{$ref_to_n2}){
		my $val = pop(@{$ref_to_n1}) + pop(@{$ref_to_n2});
		unshift(@n, ($carry + $val) % 10);
		$carry = int(($carry + $val) / 10);
	}
	my $unshift_dist = @{$ref_to_n1} + @{$ref_to_n2};
	unshift(@n, @{$ref_to_n1});
	unshift(@n, @{$ref_to_n2});
	if ($carry != 0){
		if ($unshift_dist == 0){
			unshift(@n, $carry);
		}
		else{
			$n[$unshift_dist-1] += $carry;
		}
	}
	return \@n;
}

sub subtract{
	# n1 - n2
	my ($ref_to_n1, $ref_to_n2) = @_;
	my @n;
	my $carry = 0;
	while (@{$ref_to_n1} || @{$ref_to_n2}){
		my $val = pop(@{$ref_to_n1}) - pop(@{$ref_to_n2}) - $carry;
		if ($val < 0){
			$carry = 1;
			$val += 10;
		}
		else{
			$carry = 0;
		}
		unshift(@n, $val);
	}
	shift(@n) if $n[0] == 0;
	return \@n;
}
sub from_arr_to_numeric{
	my ($ref_to_n) = @_;
	return int(join '', @{$ref_to_n});
}
sub from_numeric_to_arr{
	my ($num) = @_;
	$num .= "";
	my @num_array = split "", $num;
	return \@num_array;
}
