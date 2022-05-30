# SPDX-License-Identifier: Apache-2.0
# Copyright 2011-2022 Blender Foundation

if(WIN32)
  add_definitions(-DNOMINMAX -DWIN32_LEAN_AND_MEAN)
endif()
add_definitions(-DPXR_STATIC)

# USD headers use deprecated TBB headers, silence warning.
add_definitions(-DTBB_SUPPRESS_DEPRECATED_MESSAGES=1)

set(INC
  # ../../intern
  # ../../glew-mx
  ../../intern/guardedalloc
  # ../../mikktspace
  ../../source/blender/makesdna
  ../../source/blender/makesrna
  ../../source/blender/blenlib
  ../../source/blender/io/usd/intern
  ${CMAKE_BINARY_DIR}/source/blender/makesrna/intern
)

set(INC_SYS
  ${PYTHON_INCLUDE_DIRS}
  ${USD_INCLUDE_DIRS}
  ${BOOST_INCLUDE_DIR}
  ${TBB_INCLUDE_DIR}
)

set(SRC
  python.cpp
  session.cpp
  usd_node.cpp
  utils.cpp

  hdusd_python_api.h
  session.h
  utils.h
)

set(LIB
  ${PYTHON_LINKFLAGS}
  ${PYTHON_LIBRARIES}
  ${BOOST_LIBRARIES}
)

#if(WITH_CYCLES_LOGGING)
  list(APPEND LIB
    ${GLOG_LIBRARIES}
    ${GFLAGS_LIBRARIES}
  )
#endif()

set(ADDON_FILES
  addon/__init__.py
  addon/engine.py
  addon/handlers.py
)

set(ADDON_USD_NODES_FILES
  addon/usd_nodes/__init__.py
  addon/usd_nodes/node_tree.py
)

set(ADDON_USD_NODES_NODES_FILES
  addon/usd_nodes/nodes/__init__.py
  addon/usd_nodes/nodes/base_node.py
  addon/usd_nodes/nodes/converter.py
  addon/usd_nodes/nodes/input.py
  addon/usd_nodes/nodes/output.py
  addon/usd_nodes/nodes/transformations.py
)

set(ADDON_PROPERTIES_FILES
  addon/properties/__init__.py
  addon/properties/node.py
  addon/properties/scene.py
  addon/properties/hdrpr_render.py
  addon/properties/material.py
  addon/properties/matlib.py
  addon/properties/object.py
  addon/properties/usd_list.py
)

set(ADDON_UI_FILES
  addon/ui/__init__.py
  addon/ui/render.py
  addon/ui/hdrpr_render.py
  addon/ui/object.py
  addon/ui/world.py
  addon/ui/material.py
  addon/ui/light.py
  addon/ui/matlib.py
  addon/ui/panels.py
)

set(ADDON_UTILS_FILES
  addon/utils/__init__.py
  addon/utils/stages.py
)

set(HDUSD_INSTALL_PATH "scripts/addons/hdusd")

blender_add_lib(extern_hdusd "${SRC}" "${INC}" "${INC_SYS}" "${LIB}")

#message(FATAL_ERROR "CMAKE_CURRENT_SOURCE_DIR=${CMAKE_CURRENT_SOURCE_DIR}, CYCLES_INSTALL_PATH=${HDUSD_INSTALL_PATH}")
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_FILES}" ${HDUSD_INSTALL_PATH})
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_UTILS_FILES}" ${HDUSD_INSTALL_PATH}/utils)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_PROPERTIES_FILES}" ${HDUSD_INSTALL_PATH}/properties)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_USD_NODES_FILES}" ${HDUSD_INSTALL_PATH}/usd_nodes)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_USD_NODES_NODES_FILES}" ${HDUSD_INSTALL_PATH}/usd_nodes/nodes)
delayed_install(${CMAKE_CURRENT_SOURCE_DIR} "${ADDON_UI_FILES}" ${HDUSD_INSTALL_PATH}/ui)
