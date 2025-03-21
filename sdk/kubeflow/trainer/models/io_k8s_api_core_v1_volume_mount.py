# coding: utf-8

"""
    Kubeflow Trainer OpenAPI Spec

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: unversioned
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class IoK8sApiCoreV1VolumeMount(BaseModel):
    """
    VolumeMount describes a mounting of a Volume within a container.
    """ # noqa: E501
    mount_path: StrictStr = Field(description="Path within the container at which the volume should be mounted.  Must not contain ':'.", alias="mountPath")
    mount_propagation: Optional[StrictStr] = Field(default=None, description="mountPropagation determines how mounts are propagated from the host to container and the other way around. When not set, MountPropagationNone is used. This field is beta in 1.10. When RecursiveReadOnly is set to IfPossible or to Enabled, MountPropagation must be None or unspecified (which defaults to None).  Possible enum values:  - `\"Bidirectional\"` means that the volume in a container will receive new mounts from the host or other containers, and its own mounts will be propagated from the container to the host or other containers. Note that this mode is recursively applied to all mounts in the volume (\"rshared\" in Linux terminology).  - `\"HostToContainer\"` means that the volume in a container will receive new mounts from the host or other containers, but filesystems mounted inside the container won't be propagated to the host or other containers. Note that this mode is recursively applied to all mounts in the volume (\"rslave\" in Linux terminology).  - `\"None\"` means that the volume in a container will not receive new mounts from the host or other containers, and filesystems mounted inside the container won't be propagated to the host or other containers. Note that this mode corresponds to \"private\" in Linux terminology.", alias="mountPropagation")
    name: StrictStr = Field(description="This must match the Name of a Volume.")
    read_only: Optional[StrictBool] = Field(default=None, description="Mounted read-only if true, read-write otherwise (false or unspecified). Defaults to false.", alias="readOnly")
    recursive_read_only: Optional[StrictStr] = Field(default=None, description="RecursiveReadOnly specifies whether read-only mounts should be handled recursively.  If ReadOnly is false, this field has no meaning and must be unspecified.  If ReadOnly is true, and this field is set to Disabled, the mount is not made recursively read-only.  If this field is set to IfPossible, the mount is made recursively read-only, if it is supported by the container runtime.  If this field is set to Enabled, the mount is made recursively read-only if it is supported by the container runtime, otherwise the pod will not be started and an error will be generated to indicate the reason.  If this field is set to IfPossible or Enabled, MountPropagation must be set to None (or be unspecified, which defaults to None).  If this field is not specified, it is treated as an equivalent of Disabled.", alias="recursiveReadOnly")
    sub_path: Optional[StrictStr] = Field(default=None, description="Path within the volume from which the container's volume should be mounted. Defaults to \"\" (volume's root).", alias="subPath")
    sub_path_expr: Optional[StrictStr] = Field(default=None, description="Expanded path within the volume from which the container's volume should be mounted. Behaves similarly to SubPath but environment variable references $(VAR_NAME) are expanded using the container's environment. Defaults to \"\" (volume's root). SubPathExpr and SubPath are mutually exclusive.", alias="subPathExpr")
    __properties: ClassVar[List[str]] = ["mountPath", "mountPropagation", "name", "readOnly", "recursiveReadOnly", "subPath", "subPathExpr"]

    @field_validator('mount_propagation')
    def mount_propagation_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['Bidirectional', 'HostToContainer', 'None']):
            raise ValueError("must be one of enum values ('Bidirectional', 'HostToContainer', 'None')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1VolumeMount from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IoK8sApiCoreV1VolumeMount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mountPath": obj.get("mountPath") if obj.get("mountPath") is not None else '',
            "mountPropagation": obj.get("mountPropagation"),
            "name": obj.get("name") if obj.get("name") is not None else '',
            "readOnly": obj.get("readOnly"),
            "recursiveReadOnly": obj.get("recursiveReadOnly"),
            "subPath": obj.get("subPath"),
            "subPathExpr": obj.get("subPathExpr")
        })
        return _obj


