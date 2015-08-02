#!/usr/bin/env lua

--
-- functions
--

-- isPrime thanks to Taylor on stackoverflow http://stackoverflow.com/a/17927969/2002471
function isPrime(n)
    local n = tonumber(n)
    --catch nil, 0, 1, negative and non int numbers
    if not n or n<2 or (n % 1 ~=0) then 
        return false
    --catch even number above 2
    elseif n>2 and (n % 2 == 0) then 
        return false
    --primes over 5 end in 1,3,7 or 9
    --catch numbers that end in 5 or 0 (multiples of 5)
    elseif n>5 and (n % 5 ==0) then 
        return false
    --now check for prime
    else
        --only do the odds
        for i = 3, math.sqrt(n), 2 do
            --did it divide evenly
            if (n % i == 0) then
                return false
            end
        end
        --can defeat optimus
        return true
    end
end

if isPrime(9) then
	print("bs")
end

if isPrime(7) then
	print("good")
end

if isPrime(17) then
	print("good")
end

