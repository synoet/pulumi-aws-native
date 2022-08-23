// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * The AWS::ElasticBeanstalk::Application resource specifies an Elastic Beanstalk application.
 */
export class Application extends pulumi.CustomResource {
    /**
     * Get an existing Application resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Application {
        return new Application(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:elasticbeanstalk:Application';

    /**
     * Returns true if the given object is an instance of Application.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Application {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Application.__pulumiType;
    }

    /**
     * A name for the Elastic Beanstalk application. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name.
     */
    public readonly applicationName!: pulumi.Output<string | undefined>;
    /**
     * Your description of the application.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.
     */
    public readonly resourceLifecycleConfig!: pulumi.Output<outputs.elasticbeanstalk.ApplicationResourceLifecycleConfig | undefined>;

    /**
     * Create a Application resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ApplicationArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["applicationName"] = args ? args.applicationName : undefined;
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["resourceLifecycleConfig"] = args ? args.resourceLifecycleConfig : undefined;
        } else {
            resourceInputs["applicationName"] = undefined /*out*/;
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["resourceLifecycleConfig"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Application.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Application resource.
 */
export interface ApplicationArgs {
    /**
     * A name for the Elastic Beanstalk application. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name.
     */
    applicationName?: pulumi.Input<string>;
    /**
     * Your description of the application.
     */
    description?: pulumi.Input<string>;
    /**
     * Specifies an application resource lifecycle configuration to prevent your application from accumulating too many versions.
     */
    resourceLifecycleConfig?: pulumi.Input<inputs.elasticbeanstalk.ApplicationResourceLifecycleConfigArgs>;
}
