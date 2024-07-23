#!/usr/bin/env python3
"""
Main file for paginating data.
"""

import csv
import math
from typing import List, Tuple, Dict


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple containing a start index and an end index corresponding
    to the range of indexes to return in a list for those
    particular pagination parameters.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start and end indexes.
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of lists containing the data for
            the specified page.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Return a dictionary containing hypermedia pagination
        metadata that is resilient to deletions.

        Args:
            index (int): The starting index for the pagination.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary containing pagination metadata.
        """
        assert index is None or isinstance(index, int),
        assert isinstance(page_size, int) and page_size > 0,

        indexed_dataset = self.indexed_dataset()
        total_items = len(indexed_dataset)

        if index is None or index >= total_items:
            raise AssertionError("Index out of range")

        current_index = index
        data = []

        while len(data) < page_size and current_index < total_items:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1

        next_index = current_index if current_index < total_items else None

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
