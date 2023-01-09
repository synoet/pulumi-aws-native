// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::FSx::FileSystem
 */
export function getFileSystem(args: GetFileSystemArgs, opts?: pulumi.InvokeOptions): Promise<GetFileSystemResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:fsx:getFileSystem", {
        "id": args.id,
    }, opts);
}

export interface GetFileSystemArgs {
    id: string;
}

export interface GetFileSystemResult {
    readonly dNSName?: string;
    readonly id?: string;
    readonly lustreConfiguration?: outputs.fsx.FileSystemLustreConfiguration;
    readonly lustreMountName?: string;
    readonly ontapConfiguration?: outputs.fsx.FileSystemOntapConfiguration;
    readonly openZFSConfiguration?: outputs.fsx.FileSystemOpenZFSConfiguration;
    readonly resourceARN?: string;
    readonly rootVolumeId?: string;
    readonly storageCapacity?: number;
    readonly tags?: outputs.fsx.FileSystemTag[];
    readonly windowsConfiguration?: outputs.fsx.FileSystemWindowsConfiguration;
}

export function getFileSystemOutput(args: GetFileSystemOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetFileSystemResult> {
    return pulumi.output(args).apply(a => getFileSystem(a, opts))
}

export interface GetFileSystemOutputArgs {
    id: pulumi.Input<string>;
}
