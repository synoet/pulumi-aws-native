// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::GuardDuty::Filter
 *
 * @deprecated Filter is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Filter extends pulumi.CustomResource {
    /**
     * Get an existing Filter resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Filter {
        pulumi.log.warn("Filter is deprecated: Filter is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Filter(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:guardduty:Filter';

    /**
     * Returns true if the given object is an instance of Filter.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Filter {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Filter.__pulumiType;
    }

    public readonly action!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string>;
    public readonly detectorId!: pulumi.Output<string>;
    public readonly findingCriteria!: pulumi.Output<outputs.guardduty.FilterFindingCriteria>;
    public readonly name!: pulumi.Output<string>;
    public readonly rank!: pulumi.Output<number>;

    /**
     * Create a Filter resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Filter is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: FilterArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Filter is deprecated: Filter is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.action === undefined) && !opts.urn) {
                throw new Error("Missing required property 'action'");
            }
            if ((!args || args.description === undefined) && !opts.urn) {
                throw new Error("Missing required property 'description'");
            }
            if ((!args || args.detectorId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'detectorId'");
            }
            if ((!args || args.findingCriteria === undefined) && !opts.urn) {
                throw new Error("Missing required property 'findingCriteria'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            if ((!args || args.rank === undefined) && !opts.urn) {
                throw new Error("Missing required property 'rank'");
            }
            inputs["action"] = args ? args.action : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["detectorId"] = args ? args.detectorId : undefined;
            inputs["findingCriteria"] = args ? args.findingCriteria : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["rank"] = args ? args.rank : undefined;
        } else {
            inputs["action"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["detectorId"] = undefined /*out*/;
            inputs["findingCriteria"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["rank"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Filter.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Filter resource.
 */
export interface FilterArgs {
    action: pulumi.Input<string>;
    description: pulumi.Input<string>;
    detectorId: pulumi.Input<string>;
    findingCriteria: pulumi.Input<inputs.guardduty.FilterFindingCriteriaArgs>;
    name: pulumi.Input<string>;
    rank: pulumi.Input<number>;
}
