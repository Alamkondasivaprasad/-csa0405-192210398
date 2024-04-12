import matplotlib.pyplot as plt
import numpy as np
import random

class VirtualMemory:
    def __init__(self, num_pages, num_frames):
        self.num_pages = num_pages
        self.num_frames = num_frames
        self.page_table = {}  # Simulated page table, initially empty
        self.frames = [None] * num_frames  # Simulated physical memory

    def load_page(self, page_number):
        if page_number in self.page_table:
            frame_number = self.page_table[page_number]
            print(f"Page {page_number} already in Frame {frame_number}")
        else:
            free_frame = self.get_free_frame()
            if free_frame is not None:
                self.frames[free_frame] = page_number
                self.page_table[page_number] = free_frame
                print(f"Page {page_number} loaded into Frame {free_frame}")
            else:
                self.handle_page_fault(page_number)

    def get_free_frame(self):
        for i, frame in enumerate(self.frames):
            if frame is None:
                return i
        return None

    def handle_page_fault(self, page_number):
        # Replace a page using some algorithm (e.g., FIFO, LRU)
        # For simplicity, let's just pick a random frame to replace
        frame_to_replace = random.randint(0, self.num_frames - 1)
        old_page = self.frames[frame_to_replace]
        del self.page_table[old_page]
        self.page_table[page_number] = frame_to_replace
        self.frames[frame_to_replace] = page_number
        print(f"Page {old_page} evicted. Page {page_number} loaded into Frame {frame_to_replace}")

    def display_memory(self):
        fig, ax = plt.subplots()

        page_numbers = list(self.page_table.keys())
        frame_numbers = list(self.page_table.values())

        for i, frame_number in enumerate(self.frames):
            if frame_number is not None:
                ax.barh(i, 1, color='blue', label=f'Frame {i}: Page {frame_number}')
            else:
                ax.barh(i, 1, color='white', label=f'Frame {i}: Empty')

        ax.set_yticks(np.arange(self.num_frames))
        ax.set_yticklabels([f'Frame {i}' for i in range(self.num_frames)])
        ax.set_xlabel('Pages')
        ax.set_title('Virtual Memory')
        ax.legend()

        plt.show()

# Example usage
virtual_memory = VirtualMemory(num_pages=10, num_frames=4)
virtual_memory.load_page(0)
virtual_memory.load_page(1)
virtual_memory.load_page(2)
virtual_memory.load_page(3)
virtual_memory.load_page(4)
virtual_memory.display_memory()












