// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EC2::SnapshotBlockPublicAccess
 */
export class SnapshotBlockPublicAccess extends pulumi.CustomResource {
    /**
     * Get an existing SnapshotBlockPublicAccess resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): SnapshotBlockPublicAccess {
        return new SnapshotBlockPublicAccess(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:ec2:SnapshotBlockPublicAccess';

    /**
     * Returns true if the given object is an instance of SnapshotBlockPublicAccess.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is SnapshotBlockPublicAccess {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === SnapshotBlockPublicAccess.__pulumiType;
    }

    /**
     * The identifier for the specified AWS account.
     */
    public /*out*/ readonly accountId!: pulumi.Output<string>;
    /**
     * The state of EBS Snapshot Block Public Access.
     */
    public readonly state!: pulumi.Output<enums.ec2.SnapshotBlockPublicAccessState>;

    /**
     * Create a SnapshotBlockPublicAccess resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: SnapshotBlockPublicAccessArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.state === undefined) && !opts.urn) {
                throw new Error("Missing required property 'state'");
            }
            resourceInputs["state"] = args ? args.state : undefined;
            resourceInputs["accountId"] = undefined /*out*/;
        } else {
            resourceInputs["accountId"] = undefined /*out*/;
            resourceInputs["state"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(SnapshotBlockPublicAccess.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a SnapshotBlockPublicAccess resource.
 */
export interface SnapshotBlockPublicAccessArgs {
    /**
     * The state of EBS Snapshot Block Public Access.
     */
    state: pulumi.Input<enums.ec2.SnapshotBlockPublicAccessState>;
}
