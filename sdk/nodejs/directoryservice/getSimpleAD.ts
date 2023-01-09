// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::DirectoryService::SimpleAD
 */
export function getSimpleAD(args: GetSimpleADArgs, opts?: pulumi.InvokeOptions): Promise<GetSimpleADResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:directoryservice:getSimpleAD", {
        "directoryId": args.directoryId,
    }, opts);
}

export interface GetSimpleADArgs {
    /**
     * The unique identifier for a directory.
     */
    directoryId: string;
}

export interface GetSimpleADResult {
    /**
     * The alias for a directory.
     */
    readonly alias?: string;
    /**
     * The unique identifier for a directory.
     */
    readonly directoryId?: string;
    /**
     * The IP addresses of the DNS servers for the directory, such as [ "172.31.3.154", "172.31.63.203" ].
     */
    readonly dnsIpAddresses?: string[];
    /**
     * Whether to enable single sign-on for a Simple Active Directory in AWS.
     */
    readonly enableSso?: boolean;
}

export function getSimpleADOutput(args: GetSimpleADOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetSimpleADResult> {
    return pulumi.output(args).apply(a => getSimpleAD(a, opts))
}

export interface GetSimpleADOutputArgs {
    /**
     * The unique identifier for a directory.
     */
    directoryId: pulumi.Input<string>;
}
