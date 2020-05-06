# Copyright 2013-2020 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *
import os


class LuaLuv(CMakePackage):
    """libuv bindings for luajit and lua"""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = 'https://github.com/luvit/luv'
    url =  'https://github.com/luvit/luv/archive/1.36.0-0.tar.gz'

    version('1.36.0-0', sha256='739d733d32741a9e6caa3ff3a4416dcf121f39f622ee143c7d63130ce7de27be')

    depends_on('cmake', type='build')
    depends_on('libuv')
    depends_on('lua-luajit')
    extends('lua')

    resource(name='lua-compat-5.3',
             url='https://github.com/keplerproject/lua-compat-5.3/archive/v0.7.tar.gz',
             sha256='bec3a23114a3d9b3218038309657f0f506ad10dfbc03bb54e91da7e5ffdba0a2',
             destination='deps/',
             placement='lua-compat')

    #def patch(self):
    #    shutil.rmtree('deps/lua-compat-5.3')

    def cmake_args(self):
        args = []
        args.extend(['-DWITH_SHARED_LIBUV=ON',
                    '-DLIBUV_INCLUDE_DIR=%s'%self.spec['libuv'].prefix.include,
                    '-DLIBUV_LIBRARIES=%s'%self.spec['libuv'].prefix.lib,
                    '-DLUA_BUILD_TYPE=System',
                    '-DBUILD_SHARED_LIBS=ON',
                    '-DBUILD_MODULE=ON',
                    '-DLUA_COMPAT53_DIR=%s'%os.path.join(self.stage.source_path, 'deps/lua-compat')])

        return args

    #def install(self, spec, prefix):
    #    #luarocks('--tree=' + prefix, 'install', 'luv-1.36.0-0.src.rock')
    #    luarocks('--tree=' + prefix, 'install', 'luv-scm-0.rockspec',
    #             '-DWITH_SHARED_LIBUV=ON',
    #             '-DLIBUV_INCLUDE_DIR=%s'%self.spec['libuv'].prefix.include,
    #             '-DLIBUV_LIBRARIES=%s'%self.spec['libuv'].prefix.lib)
