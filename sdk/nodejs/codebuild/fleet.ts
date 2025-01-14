// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::CodeBuild::Fleet
 */
export class Fleet extends pulumi.CustomResource {
    /**
     * Get an existing Fleet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Fleet {
        return new Fleet(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:codebuild:Fleet';

    /**
     * Returns true if the given object is an instance of Fleet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Fleet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Fleet.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly baseCapacity!: pulumi.Output<number | undefined>;
    public readonly computeType!: pulumi.Output<enums.codebuild.FleetComputeType | undefined>;
    public readonly environmentType!: pulumi.Output<enums.codebuild.FleetEnvironmentType | undefined>;
    public readonly name!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.codebuild.FleetTag[] | undefined>;

    /**
     * Create a Fleet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: FleetArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["baseCapacity"] = args ? args.baseCapacity : undefined;
            resourceInputs["computeType"] = args ? args.computeType : undefined;
            resourceInputs["environmentType"] = args ? args.environmentType : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["arn"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["baseCapacity"] = undefined /*out*/;
            resourceInputs["computeType"] = undefined /*out*/;
            resourceInputs["environmentType"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Fleet.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Fleet resource.
 */
export interface FleetArgs {
    baseCapacity?: pulumi.Input<number>;
    computeType?: pulumi.Input<enums.codebuild.FleetComputeType>;
    environmentType?: pulumi.Input<enums.codebuild.FleetEnvironmentType>;
    name?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.codebuild.FleetTagArgs>[]>;
}
