// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Aws Route53 Recovery Readiness Check Schema and API specification.
 */
export class ReadinessCheck extends pulumi.CustomResource {
    /**
     * Get an existing ReadinessCheck resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): ReadinessCheck {
        return new ReadinessCheck(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:route53recoveryreadiness:ReadinessCheck';

    /**
     * Returns true if the given object is an instance of ReadinessCheck.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ReadinessCheck {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ReadinessCheck.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the readiness check.
     */
    public /*out*/ readonly readinessCheckArn!: pulumi.Output<string>;
    /**
     * Name of the ReadinessCheck to create.
     */
    public readonly readinessCheckName!: pulumi.Output<string>;
    /**
     * The name of the resource set to check.
     */
    public readonly resourceSetName!: pulumi.Output<string | undefined>;
    /**
     * A collection of tags associated with a resource.
     */
    public readonly tags!: pulumi.Output<outputs.route53recoveryreadiness.ReadinessCheckTag[] | undefined>;

    /**
     * Create a ReadinessCheck resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ReadinessCheckArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            inputs["readinessCheckName"] = args ? args.readinessCheckName : undefined;
            inputs["resourceSetName"] = args ? args.resourceSetName : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["readinessCheckArn"] = undefined /*out*/;
        } else {
            inputs["readinessCheckArn"] = undefined /*out*/;
            inputs["readinessCheckName"] = undefined /*out*/;
            inputs["resourceSetName"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(ReadinessCheck.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a ReadinessCheck resource.
 */
export interface ReadinessCheckArgs {
    /**
     * Name of the ReadinessCheck to create.
     */
    readinessCheckName?: pulumi.Input<string>;
    /**
     * The name of the resource set to check.
     */
    resourceSetName?: pulumi.Input<string>;
    /**
     * A collection of tags associated with a resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.route53recoveryreadiness.ReadinessCheckTagArgs>[]>;
}
