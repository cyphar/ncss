#!/usr/bin/env python3
# Enter your code for "GrokCoins" here.

import functools

def memoise(func):
	lookup = {}

	# As it turns out, the Grok marker cannot deal with variadric (or star magic)
	# arguments (since they check the value of <func>.__code__.co_argcount). As a
	# result, I've used a single argument (when you're *supposed* to use *args).

	@functools.wraps(func)
	def wrapper(coin):
		# Check in lookup table. Lookups are cheap, computation is not.
		if coin in lookup:
			return lookup[coin]

		# Calculate and store result in lookup table.
		ret = func(coin)
		lookup[coin] = ret
		return ret

	# Closures are magical.
	return wrapper

@memoise
def convert_grokcoin(coin):
	# Split up the coins.
	coins = [coin//2, coin//3, coin//4]

	# We have already hit the largest, bail!
	if sum(coins) <= coin:
		return coin

	# Recurse.
	return sum(convert_grokcoin(coin) for coin in coins)
