// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const StreamStreamEncryptionEncryptionType = {
    Kms: "KMS",
} as const;

/**
 * The encryption type to use. The only valid value is KMS. 
 */
export type StreamStreamEncryptionEncryptionType = (typeof StreamStreamEncryptionEncryptionType)[keyof typeof StreamStreamEncryptionEncryptionType];
