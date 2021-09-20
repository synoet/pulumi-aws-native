// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const SchemaCompatibility = {
    None: "NONE",
    Disabled: "DISABLED",
    Backward: "BACKWARD",
    BackwardAll: "BACKWARD_ALL",
    Forward: "FORWARD",
    ForwardAll: "FORWARD_ALL",
    Full: "FULL",
    FullAll: "FULL_ALL",
} as const;

/**
 * Compatibility setting for the schema.
 */
export type SchemaCompatibility = (typeof SchemaCompatibility)[keyof typeof SchemaCompatibility];

export const SchemaDataFormat = {
    Avro: "AVRO",
    Json: "JSON",
} as const;

/**
 * Data format name to use for the schema. Accepted values: 'AVRO', 'JSON'
 */
export type SchemaDataFormat = (typeof SchemaDataFormat)[keyof typeof SchemaDataFormat];
