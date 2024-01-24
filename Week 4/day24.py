"""
Day 24: Generators (Advanced)

Dive deeper into generators and explore asynchronous generators and generator expressions.

Useful for:
-I/O Bound Operations
-Web Scraping and API requests
-Concurrency and Parallelism
-GUI Applications
-Real Time Applications
-Event Driven Programming
-Periodic Task
"""

# Example 1: Asynchronous Generators

import asyncio

async def async_generator():
    for i in range(5):
        await asyncio.sleep(1)  # Simulate asynchronous operation
        yield i

async def main_async():
    async for value in async_generator():
        print("Async:", value)

# Example 2: Generator Expression

# Generator expression to generate squares of numbers
squares = (x ** 2 for x in range(5))

# Example 3: Consuming the Generator Expression
def consume_generator_expression():
    for square in squares:
        print("Generator Expression:", square)

# Run the examples
if __name__ == "__main__":
    # Run the asynchronous generator example
    asyncio.run(main_async())

    # Run the generator expression example
    consume_generator_expression()
