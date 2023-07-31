// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const CampaignCompression = {
    Off: "OFF",
    Snappy: "SNAPPY",
} as const;

export type CampaignCompression = (typeof CampaignCompression)[keyof typeof CampaignCompression];

export const CampaignDataFormat = {
    Json: "JSON",
    Parquet: "PARQUET",
} as const;

export type CampaignDataFormat = (typeof CampaignDataFormat)[keyof typeof CampaignDataFormat];

export const CampaignDiagnosticsMode = {
    Off: "OFF",
    SendActiveDtcs: "SEND_ACTIVE_DTCS",
} as const;

export type CampaignDiagnosticsMode = (typeof CampaignDiagnosticsMode)[keyof typeof CampaignDiagnosticsMode];

export const CampaignSpoolingMode = {
    Off: "OFF",
    ToDisk: "TO_DISK",
} as const;

export type CampaignSpoolingMode = (typeof CampaignSpoolingMode)[keyof typeof CampaignSpoolingMode];

export const CampaignStatus = {
    Creating: "CREATING",
    WaitingForApproval: "WAITING_FOR_APPROVAL",
    Running: "RUNNING",
    Suspended: "SUSPENDED",
} as const;

export type CampaignStatus = (typeof CampaignStatus)[keyof typeof CampaignStatus];

export const CampaignStorageCompressionFormat = {
    None: "NONE",
    Gzip: "GZIP",
} as const;

export type CampaignStorageCompressionFormat = (typeof CampaignStorageCompressionFormat)[keyof typeof CampaignStorageCompressionFormat];

export const CampaignTriggerMode = {
    Always: "ALWAYS",
    RisingEdge: "RISING_EDGE",
} as const;

export type CampaignTriggerMode = (typeof CampaignTriggerMode)[keyof typeof CampaignTriggerMode];

export const CampaignUpdateCampaignAction = {
    Approve: "APPROVE",
    Suspend: "SUSPEND",
    Resume: "RESUME",
    Update: "UPDATE",
} as const;

export type CampaignUpdateCampaignAction = (typeof CampaignUpdateCampaignAction)[keyof typeof CampaignUpdateCampaignAction];

export const DecoderManifestCanNetworkInterfaceType = {
    CanInterface: "CAN_INTERFACE",
} as const;

export type DecoderManifestCanNetworkInterfaceType = (typeof DecoderManifestCanNetworkInterfaceType)[keyof typeof DecoderManifestCanNetworkInterfaceType];

export const DecoderManifestCanSignalDecoderType = {
    CanSignal: "CAN_SIGNAL",
} as const;

export type DecoderManifestCanSignalDecoderType = (typeof DecoderManifestCanSignalDecoderType)[keyof typeof DecoderManifestCanSignalDecoderType];

export const DecoderManifestManifestStatus = {
    Active: "ACTIVE",
    Draft: "DRAFT",
} as const;

export type DecoderManifestManifestStatus = (typeof DecoderManifestManifestStatus)[keyof typeof DecoderManifestManifestStatus];

export const DecoderManifestObdNetworkInterfaceType = {
    ObdInterface: "OBD_INTERFACE",
} as const;

export type DecoderManifestObdNetworkInterfaceType = (typeof DecoderManifestObdNetworkInterfaceType)[keyof typeof DecoderManifestObdNetworkInterfaceType];

export const DecoderManifestObdSignalDecoderType = {
    ObdSignal: "OBD_SIGNAL",
} as const;

export type DecoderManifestObdSignalDecoderType = (typeof DecoderManifestObdSignalDecoderType)[keyof typeof DecoderManifestObdSignalDecoderType];

export const ModelManifestManifestStatus = {
    Active: "ACTIVE",
    Draft: "DRAFT",
} as const;

export type ModelManifestManifestStatus = (typeof ModelManifestManifestStatus)[keyof typeof ModelManifestManifestStatus];

export const SignalCatalogNodeDataType = {
    Int8: "INT8",
    Uint8: "UINT8",
    Int16: "INT16",
    Uint16: "UINT16",
    Int32: "INT32",
    Uint32: "UINT32",
    Int64: "INT64",
    Uint64: "UINT64",
    Boolean: "BOOLEAN",
    Float: "FLOAT",
    Double: "DOUBLE",
    String: "STRING",
    UnixTimestamp: "UNIX_TIMESTAMP",
    Int8Array: "INT8_ARRAY",
    Uint8Array: "UINT8_ARRAY",
    Int16Array: "INT16_ARRAY",
    Uint16Array: "UINT16_ARRAY",
    Int32Array: "INT32_ARRAY",
    Uint32Array: "UINT32_ARRAY",
    Int64Array: "INT64_ARRAY",
    Uint64Array: "UINT64_ARRAY",
    BooleanArray: "BOOLEAN_ARRAY",
    FloatArray: "FLOAT_ARRAY",
    DoubleArray: "DOUBLE_ARRAY",
    StringArray: "STRING_ARRAY",
    UnixTimestampArray: "UNIX_TIMESTAMP_ARRAY",
    Unknown: "UNKNOWN",
} as const;

export type SignalCatalogNodeDataType = (typeof SignalCatalogNodeDataType)[keyof typeof SignalCatalogNodeDataType];

export const VehicleAssociationBehavior = {
    CreateIotThing: "CreateIotThing",
    ValidateIotThingExists: "ValidateIotThingExists",
} as const;

export type VehicleAssociationBehavior = (typeof VehicleAssociationBehavior)[keyof typeof VehicleAssociationBehavior];
