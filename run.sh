#!/usr/bin/env bash
SRC_DIR=.
DST_DIR=.
PROTO_FILE=$1

protoc -I=$SRC_DIR --python_out=$DST_DIR $PROTO_FILE

echo "Google protocol Buffer $PROTO_FILE created. "
