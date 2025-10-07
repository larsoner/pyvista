"""PyVista package for 3D plotting and mesh analysis."""

from __future__ import annotations

import os
import sys
from typing import TYPE_CHECKING
from typing import Literal

from pyvista._plot import plot as plot
from pyvista._version import __version__ as __version__
from pyvista._version import version_info as version_info
from pyvista.core import *
from pyvista.core import _validation as _validation
from pyvista.core._typing_core._dataset_types import _DataObjectType as _DataObjectType
from pyvista.core._typing_core._dataset_types import (
    _DataSetOrMultiBlockType as _DataSetOrMultiBlockType,
)
from pyvista.core._typing_core._dataset_types import _DataSetType as _DataSetType
from pyvista.core._typing_core._dataset_types import _GridType as _GridType
from pyvista.core._typing_core._dataset_types import _PointGridType as _PointGridType
from pyvista.core._typing_core._dataset_types import _PointSetType as _PointSetType
from pyvista.core._vtk_core import _MIN_SUPPORTED_VTK_VERSION
from pyvista.core._vtk_core import VersionInfo
from pyvista.core._vtk_core import vtk_version_info as vtk_version_info
from pyvista.core.cell import _get_vtk_id_type
from pyvista.core.utilities.observers import send_errors_to_logging
from pyvista.core.wrappers import _wrappers as _wrappers
from pyvista.jupyter import JupyterBackendOptions as JupyterBackendOptions
from pyvista.jupyter import set_jupyter_backend as set_jupyter_backend
from pyvista.report import GPUInfo as GPUInfo
from pyvista.report import Report as Report
from pyvista.report import check_math_text_support as check_math_text_support
from pyvista.report import check_matplotlib_vtk_compatibility as check_matplotlib_vtk_compatibility
from pyvista.report import get_gpu_info as get_gpu_info
