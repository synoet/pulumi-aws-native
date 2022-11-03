// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::Volume
 */
export function getVolume(args: GetVolumeArgs, opts?: pulumi.InvokeOptions): Promise<GetVolumeResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:ec2:getVolume", {
        "volumeId": args.volumeId,
    }, opts);
}

export interface GetVolumeArgs {
    volumeId: string;
}

export interface GetVolumeResult {
    /**
     * The Availability Zone in which to create the volume.
     */
    readonly autoEnableIO?: boolean;
    /**
     * The number of I/O operations per second (IOPS) to provision for an io1 or io2 volume, with a maximum ratio of 50 IOPS/GiB for io1, and 500 IOPS/GiB for io2. Range is 100 to 64,000 IOPS for volumes in most Regions. Maximum IOPS of 64,000 is guaranteed only on Nitro-based instances. Other instance families guarantee performance up to 32,000 IOPS. For more information, see Amazon EBS volume types in the Amazon Elastic Compute Cloud User Guide. This parameter is valid only for Provisioned IOPS SSD (io1 and io2) volumes. 
     */
    readonly iops?: number;
    /**
     * Indicates whether Amazon EBS Multi-Attach is enabled.
     */
    readonly multiAttachEnabled?: boolean;
    /**
     * The Amazon Resource Name (ARN) of the Outpost.
     */
    readonly outpostArn?: string;
    /**
     * The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size.  Constraints: 1-16,384 for gp2, 4-16,384 for io1 and io2, 500-16,384 for st1, 500-16,384 for sc1, and 1-1,024 for standard. If you specify a snapshot, the volume size must be equal to or larger than the snapshot size. Default: If you're creating the volume from a snapshot and don't specify a volume size, the default is the snapshot size. 
     */
    readonly size?: number;
    /**
     * The tags to apply to the volume during creation.
     */
    readonly tags?: outputs.ec2.VolumeTag[];
    /**
     * The throughput that the volume supports, in MiB/s.
     */
    readonly throughput?: number;
    readonly volumeId?: string;
    /**
     * The volume type. This parameter can be one of the following values: General Purpose SSD: gp2 | gp3, Provisioned IOPS SSD: io1 | io2, Throughput Optimized HDD: st1, Cold HDD: sc1, Magnetic: standard
     */
    readonly volumeType?: string;
}

export function getVolumeOutput(args: GetVolumeOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetVolumeResult> {
    return pulumi.output(args).apply(a => getVolume(a, opts))
}

export interface GetVolumeOutputArgs {
    volumeId: pulumi.Input<string>;
}
