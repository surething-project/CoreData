# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: loc_endorse.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from . import loc_time_pb2 as loc__time__pb2
from . import signature_pb2 as signature__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='loc_endorse.proto',
  package='eu.surething_project.core',
  syntax='proto3',
  serialized_options=b'\n\031eu.surething_project.coreB\017LocEndorseProtoP\001',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x11loc_endorse.proto\x12\x19\x65u.surething_project.core\x1a\x19google/protobuf/any.proto\x1a\x0eloc_time.proto\x1a\x0fsignature.proto\"\xa6\x01\n\x13LocationEndorsement\x12\x11\n\twitnessId\x18\x01 \x01(\t\x12\x0f\n\x07\x63laimId\x18\x02 \x01(\t\x12-\n\x04time\x18\x03 \x01(\x0b\x32\x1f.eu.surething_project.core.Time\x12\x14\n\x0c\x65videnceType\x18\x04 \x01(\t\x12&\n\x08\x65vidence\x18\x05 \x01(\x0b\x32\x14.google.protobuf.Any\"\xa0\x01\n\x19SignedLocationEndorsement\x12\x43\n\x0b\x65ndorsement\x18\x01 \x01(\x0b\x32..eu.surething_project.core.LocationEndorsement\x12>\n\x10witnessSignature\x18\x02 \x01(\x0b\x32$.eu.surething_project.core.SignatureB.\n\x19\x65u.surething_project.coreB\x0fLocEndorseProtoP\x01\x62\x06proto3'
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,loc__time__pb2.DESCRIPTOR,signature__pb2.DESCRIPTOR,])




_LOCATIONENDORSEMENT = _descriptor.Descriptor(
  name='LocationEndorsement',
  full_name='eu.surething_project.core.LocationEndorsement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='witnessId', full_name='eu.surething_project.core.LocationEndorsement.witnessId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='claimId', full_name='eu.surething_project.core.LocationEndorsement.claimId', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='time', full_name='eu.surething_project.core.LocationEndorsement.time', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evidenceType', full_name='eu.surething_project.core.LocationEndorsement.evidenceType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='evidence', full_name='eu.surething_project.core.LocationEndorsement.evidence', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=275,
)


_SIGNEDLOCATIONENDORSEMENT = _descriptor.Descriptor(
  name='SignedLocationEndorsement',
  full_name='eu.surething_project.core.SignedLocationEndorsement',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='endorsement', full_name='eu.surething_project.core.SignedLocationEndorsement.endorsement', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='witnessSignature', full_name='eu.surething_project.core.SignedLocationEndorsement.witnessSignature', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=278,
  serialized_end=438,
)

_LOCATIONENDORSEMENT.fields_by_name['time'].message_type = loc__time__pb2._TIME
_LOCATIONENDORSEMENT.fields_by_name['evidence'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_SIGNEDLOCATIONENDORSEMENT.fields_by_name['endorsement'].message_type = _LOCATIONENDORSEMENT
_SIGNEDLOCATIONENDORSEMENT.fields_by_name['witnessSignature'].message_type = signature__pb2._SIGNATURE
DESCRIPTOR.message_types_by_name['LocationEndorsement'] = _LOCATIONENDORSEMENT
DESCRIPTOR.message_types_by_name['SignedLocationEndorsement'] = _SIGNEDLOCATIONENDORSEMENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LocationEndorsement = _reflection.GeneratedProtocolMessageType('LocationEndorsement', (_message.Message,), {
  'DESCRIPTOR' : _LOCATIONENDORSEMENT,
  '__module__' : 'loc_endorse_pb2'
  # @@protoc_insertion_point(class_scope:eu.surething_project.core.LocationEndorsement)
  })
_sym_db.RegisterMessage(LocationEndorsement)

SignedLocationEndorsement = _reflection.GeneratedProtocolMessageType('SignedLocationEndorsement', (_message.Message,), {
  'DESCRIPTOR' : _SIGNEDLOCATIONENDORSEMENT,
  '__module__' : 'loc_endorse_pb2'
  # @@protoc_insertion_point(class_scope:eu.surething_project.core.SignedLocationEndorsement)
  })
_sym_db.RegisterMessage(SignedLocationEndorsement)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
