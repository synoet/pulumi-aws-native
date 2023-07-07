// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * The AWS::EC2::KeyPair creates an SSH key pair
 */
export function getKeyPair(args: GetKeyPairArgs, opts?: pulumi.InvokeOptions): Promise<GetKeyPairResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getKeyPair", {
        "keyName": args.keyName,
    }, opts);
}

export interface GetKeyPairArgs {
    /**
     * The name of the SSH key pair
     */
    keyName: string;
}

export interface GetKeyPairResult {
    /**
     * A short sequence of bytes used for public key verification
     */
    readonly keyFingerprint?: string;
    /**
     * An AWS generated ID for the key pair
     */
    readonly keyPairId?: string;
}
/**
 * The AWS::EC2::KeyPair creates an SSH key pair
 */
export function getKeyPairOutput(args: GetKeyPairOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetKeyPairResult> {
    return pulumi.output(args).apply((a: any) => getKeyPair(a, opts))
}

export interface GetKeyPairOutputArgs {
    /**
     * The name of the SSH key pair
     */
    keyName: pulumi.Input<string>;
}
