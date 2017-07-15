# -*- coding: utf-8 -*-

from iscc_bench.readers.bxbooks import bxbooks
from iscc_bench.readers.dnbrdf import dnbrdf
from iscc_bench.readers.harvard import harvard
from iscc_bench.readers.openlibrary import openlibrary
from iscc_bench.readers.libgen import libgen


ALL_READERS = (bxbooks, dnbrdf, harvard, openlibrary, libgen)
