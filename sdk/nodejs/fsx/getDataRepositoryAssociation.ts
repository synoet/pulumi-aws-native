// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::FSx::DataRepositoryAssociation
 */
export function getDataRepositoryAssociation(args: GetDataRepositoryAssociationArgs, opts?: pulumi.InvokeOptions): Promise<GetDataRepositoryAssociationResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:fsx:getDataRepositoryAssociation", {
        "associationId": args.associationId,
    }, opts);
}

export interface GetDataRepositoryAssociationArgs {
    /**
     * The system-generated, unique ID of the data repository association.
     */
    associationId: string;
}

export interface GetDataRepositoryAssociationResult {
    /**
     * The system-generated, unique ID of the data repository association.
     */
    readonly associationId?: string;
    /**
     * For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.
     */
    readonly importedFileChunkSize?: number;
    /**
     * The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see Amazon Resource Names (ARNs) in the Amazon Web Services General Reference.
     */
    readonly resourceArn?: string;
    /**
     * The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.
     */
    readonly s3?: outputs.fsx.DataRepositoryAssociationS3;
    /**
     * A list of Tag values, with a maximum of 50 elements.
     */
    readonly tags?: outputs.fsx.DataRepositoryAssociationTag[];
}
/**
 * Resource Type definition for AWS::FSx::DataRepositoryAssociation
 */
export function getDataRepositoryAssociationOutput(args: GetDataRepositoryAssociationOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetDataRepositoryAssociationResult> {
    return pulumi.output(args).apply((a: any) => getDataRepositoryAssociation(a, opts))
}

export interface GetDataRepositoryAssociationOutputArgs {
    /**
     * The system-generated, unique ID of the data repository association.
     */
    associationId: pulumi.Input<string>;
}
