# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: src/core/id_generator.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bsrc/core/id_generator.proto\x12\x0bidgenerator\"#\n\x0fGenerateRequest\x12\x10\n\x08instance\x18\x01 \x01(\x05\"\x1e\n\x10GenerateResponse\x12\n\n\x02id\x18\x01 \x01(\t2X\n\x0bIDGenerator\x12I\n\x08Generate\x12\x1c.idgenerator.GenerateRequest\x1a\x1d.idgenerator.GenerateResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.core.id_generator_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_GENERATEREQUEST']._serialized_start=44
  _globals['_GENERATEREQUEST']._serialized_end=79
  _globals['_GENERATERESPONSE']._serialized_start=81
  _globals['_GENERATERESPONSE']._serialized_end=111
  _globals['_IDGENERATOR']._serialized_start=113
  _globals['_IDGENERATOR']._serialized_end=201
# @@protoc_insertion_point(module_scope)
