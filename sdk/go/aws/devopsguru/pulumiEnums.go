// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package devopsguru

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The type of ResourceCollection
type ResourceCollectionResourceCollectionType string

const (
	ResourceCollectionResourceCollectionTypeAwsCloudFormation = ResourceCollectionResourceCollectionType("AWS_CLOUD_FORMATION")
)

func (ResourceCollectionResourceCollectionType) ElementType() reflect.Type {
	return reflect.TypeOf((*ResourceCollectionResourceCollectionType)(nil)).Elem()
}

func (e ResourceCollectionResourceCollectionType) ToResourceCollectionResourceCollectionTypeOutput() ResourceCollectionResourceCollectionTypeOutput {
	return pulumi.ToOutput(e).(ResourceCollectionResourceCollectionTypeOutput)
}

func (e ResourceCollectionResourceCollectionType) ToResourceCollectionResourceCollectionTypeOutputWithContext(ctx context.Context) ResourceCollectionResourceCollectionTypeOutput {
	return pulumi.ToOutputWithContext(ctx, e).(ResourceCollectionResourceCollectionTypeOutput)
}

func (e ResourceCollectionResourceCollectionType) ToResourceCollectionResourceCollectionTypePtrOutput() ResourceCollectionResourceCollectionTypePtrOutput {
	return e.ToResourceCollectionResourceCollectionTypePtrOutputWithContext(context.Background())
}

func (e ResourceCollectionResourceCollectionType) ToResourceCollectionResourceCollectionTypePtrOutputWithContext(ctx context.Context) ResourceCollectionResourceCollectionTypePtrOutput {
	return ResourceCollectionResourceCollectionType(e).ToResourceCollectionResourceCollectionTypeOutputWithContext(ctx).ToResourceCollectionResourceCollectionTypePtrOutputWithContext(ctx)
}

func (e ResourceCollectionResourceCollectionType) ToStringOutput() pulumi.StringOutput {
	return pulumi.ToOutput(pulumi.String(e)).(pulumi.StringOutput)
}

func (e ResourceCollectionResourceCollectionType) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return pulumi.ToOutputWithContext(ctx, pulumi.String(e)).(pulumi.StringOutput)
}

func (e ResourceCollectionResourceCollectionType) ToStringPtrOutput() pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringPtrOutputWithContext(context.Background())
}

func (e ResourceCollectionResourceCollectionType) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return pulumi.String(e).ToStringOutputWithContext(ctx).ToStringPtrOutputWithContext(ctx)
}

type ResourceCollectionResourceCollectionTypeOutput struct{ *pulumi.OutputState }

func (ResourceCollectionResourceCollectionTypeOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ResourceCollectionResourceCollectionType)(nil)).Elem()
}

func (o ResourceCollectionResourceCollectionTypeOutput) ToResourceCollectionResourceCollectionTypeOutput() ResourceCollectionResourceCollectionTypeOutput {
	return o
}

func (o ResourceCollectionResourceCollectionTypeOutput) ToResourceCollectionResourceCollectionTypeOutputWithContext(ctx context.Context) ResourceCollectionResourceCollectionTypeOutput {
	return o
}

func (o ResourceCollectionResourceCollectionTypeOutput) ToResourceCollectionResourceCollectionTypePtrOutput() ResourceCollectionResourceCollectionTypePtrOutput {
	return o.ToResourceCollectionResourceCollectionTypePtrOutputWithContext(context.Background())
}

func (o ResourceCollectionResourceCollectionTypeOutput) ToResourceCollectionResourceCollectionTypePtrOutputWithContext(ctx context.Context) ResourceCollectionResourceCollectionTypePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v ResourceCollectionResourceCollectionType) *ResourceCollectionResourceCollectionType {
		return &v
	}).(ResourceCollectionResourceCollectionTypePtrOutput)
}

func (o ResourceCollectionResourceCollectionTypeOutput) ToStringOutput() pulumi.StringOutput {
	return o.ToStringOutputWithContext(context.Background())
}

func (o ResourceCollectionResourceCollectionTypeOutput) ToStringOutputWithContext(ctx context.Context) pulumi.StringOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ResourceCollectionResourceCollectionType) string {
		return string(e)
	}).(pulumi.StringOutput)
}

func (o ResourceCollectionResourceCollectionTypeOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ResourceCollectionResourceCollectionTypeOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e ResourceCollectionResourceCollectionType) *string {
		v := string(e)
		return &v
	}).(pulumi.StringPtrOutput)
}

type ResourceCollectionResourceCollectionTypePtrOutput struct{ *pulumi.OutputState }

func (ResourceCollectionResourceCollectionTypePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ResourceCollectionResourceCollectionType)(nil)).Elem()
}

func (o ResourceCollectionResourceCollectionTypePtrOutput) ToResourceCollectionResourceCollectionTypePtrOutput() ResourceCollectionResourceCollectionTypePtrOutput {
	return o
}

func (o ResourceCollectionResourceCollectionTypePtrOutput) ToResourceCollectionResourceCollectionTypePtrOutputWithContext(ctx context.Context) ResourceCollectionResourceCollectionTypePtrOutput {
	return o
}

func (o ResourceCollectionResourceCollectionTypePtrOutput) Elem() ResourceCollectionResourceCollectionTypeOutput {
	return o.ApplyT(func(v *ResourceCollectionResourceCollectionType) ResourceCollectionResourceCollectionType {
		if v != nil {
			return *v
		}
		var ret ResourceCollectionResourceCollectionType
		return ret
	}).(ResourceCollectionResourceCollectionTypeOutput)
}

func (o ResourceCollectionResourceCollectionTypePtrOutput) ToStringPtrOutput() pulumi.StringPtrOutput {
	return o.ToStringPtrOutputWithContext(context.Background())
}

func (o ResourceCollectionResourceCollectionTypePtrOutput) ToStringPtrOutputWithContext(ctx context.Context) pulumi.StringPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, e *ResourceCollectionResourceCollectionType) *string {
		if e == nil {
			return nil
		}
		v := string(*e)
		return &v
	}).(pulumi.StringPtrOutput)
}

// ResourceCollectionResourceCollectionTypeInput is an input type that accepts ResourceCollectionResourceCollectionTypeArgs and ResourceCollectionResourceCollectionTypeOutput values.
// You can construct a concrete instance of `ResourceCollectionResourceCollectionTypeInput` via:
//
//          ResourceCollectionResourceCollectionTypeArgs{...}
type ResourceCollectionResourceCollectionTypeInput interface {
	pulumi.Input

	ToResourceCollectionResourceCollectionTypeOutput() ResourceCollectionResourceCollectionTypeOutput
	ToResourceCollectionResourceCollectionTypeOutputWithContext(context.Context) ResourceCollectionResourceCollectionTypeOutput
}

var resourceCollectionResourceCollectionTypePtrType = reflect.TypeOf((**ResourceCollectionResourceCollectionType)(nil)).Elem()

type ResourceCollectionResourceCollectionTypePtrInput interface {
	pulumi.Input

	ToResourceCollectionResourceCollectionTypePtrOutput() ResourceCollectionResourceCollectionTypePtrOutput
	ToResourceCollectionResourceCollectionTypePtrOutputWithContext(context.Context) ResourceCollectionResourceCollectionTypePtrOutput
}

type resourceCollectionResourceCollectionTypePtr string

func ResourceCollectionResourceCollectionTypePtr(v string) ResourceCollectionResourceCollectionTypePtrInput {
	return (*resourceCollectionResourceCollectionTypePtr)(&v)
}

func (*resourceCollectionResourceCollectionTypePtr) ElementType() reflect.Type {
	return resourceCollectionResourceCollectionTypePtrType
}

func (in *resourceCollectionResourceCollectionTypePtr) ToResourceCollectionResourceCollectionTypePtrOutput() ResourceCollectionResourceCollectionTypePtrOutput {
	return pulumi.ToOutput(in).(ResourceCollectionResourceCollectionTypePtrOutput)
}

func (in *resourceCollectionResourceCollectionTypePtr) ToResourceCollectionResourceCollectionTypePtrOutputWithContext(ctx context.Context) ResourceCollectionResourceCollectionTypePtrOutput {
	return pulumi.ToOutputWithContext(ctx, in).(ResourceCollectionResourceCollectionTypePtrOutput)
}

func init() {
	pulumi.RegisterOutputType(ResourceCollectionResourceCollectionTypeOutput{})
	pulumi.RegisterOutputType(ResourceCollectionResourceCollectionTypePtrOutput{})
}
