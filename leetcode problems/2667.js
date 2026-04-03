/*
2667. Create Hello World Function
Solved
Easy
Companies
Write a function createHelloWorld. It should return a new function that always returns "Hello World".
 

Example 1:

Input: args = []
Output: "Hello World"
Explanation:
const f = createHelloWorld();
f(); // "Hello World"

The function returned by createHelloWorld should always return "Hello World".
Example 2:

Input: args = [{},null,42]
Output: "Hello World"
Explanation:
const f = createHelloWorld();
f({}, null, 42); // "Hello World"

Any arguments could be passed to the function but it should still always return "Hello World".
 

Constraints:

0 <= args.length <= 10
*/

/**
 * @return {Function}
 */

/*
Variant 1:
Below is my first attempt at solving this JS "Hello World" problem after reading the Editorial
Section, which introduces basic JS function syntax, and this solution was accepted! Woo hoo!
The time and space complexity are both O(1) since no data structures are used to store
information and since no loops occur within inner or outer function. This solution beats ~55%
and ~22% of accepted answers in terms of RT and memory efficiency, respectively. So not too
shabby for our first LC problem in a new language (even if it's the easiest problem known to 
mankind)!
*/

var createHelloWorld = function() {
    
    return function(...args) {
        return "Hello World"
    }
};

/**
 * const f = createHelloWorld();
 * f(); // "Hello World"
 */


/*
Variant 2:
The official solution given by LC for this problem using 'Function Syntax'. I am not sure if
there is any difference between this and Variant 1 other than syntax, and if that results in
any noticeable difference in physical performance, but this solution appears to beat ~60% and
~30% of accepted answers in terms of RT and memory efficiency respectively, so that might be
due to stasticical variance, or a slightly more efficient function. 
*/

var createHelloWorld = function() {
    return function() {
        return "Hello World";
    }
};


/*
Variant 3:
The official solution given by LC for this problem using 'Arrow Syntax'. I am not sure if
there is any difference between this and Variants 1/2 other than syntax, and if that would result 
in any noticeable difference in physical performance, but this solution appears to beat ~55% and
~35% of accepted answers in terms of RT and memory efficiency respectively, so that might be
due to stasticical variance, or a slightly different function in terms of real computing efficiency.
*/

var createHelloWorld = function() {
    return () => "Hello World";
};


/*
Variant 4:
The official solution given by LC for this problem using 'Arrow Syntax + Rest Arguments'. I am not 
sure if there is any difference between this and Variants 1/2/3 other than syntax, and if that would 
result in any noticeable difference in physical performance, but this solution appears to beat ~55% 
and ~45% of accepted answers in terms of RT and memory efficiency respectively, so that might be due 
to stasticical variance, or a slightly different function in terms of real computing efficiency.
*/

var createHelloWorld = function() {
    return (...args) => "Hello World";
};

/*
Whatever the physical difference is between the above 4 variants in terms of computing efficiency,
all 4 have O(1) complexity in both time and space. And why wouldn't they? We are simply returning
"Hello World" to the console! 